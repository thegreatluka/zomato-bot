from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, AllSlotsReset
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import zomatopy
import json
import re

config = {"user_key": "acfcf315ed54c498179910378808b0c7"}
DEFAULT_DATA_PATH = 'data'

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):

		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')

		location_detail = zomato.get_location(loc, 1)
		location_json = json.loads(location_detail)
		lat = location_json["location_suggestions"][0]["latitude"]
		lon = location_json["location_suggestions"][0]["longitude"]

		# Get {CuisineId:CuisineName} mapping for given City.
		cityId = location_json['location_suggestions'][0]['city_id']
		cuisine_dict = zomato.get_cuisines(cityId)
		cuisine_dict = dict((k, v.lower()) for k, v in cuisine_dict.items())
		cuisineId = list(cuisine_dict.keys())[list(
			cuisine_dict.values()).index(cuisine.lower())]

		results = zomato.restaurant_search(
			"", lat, lon, str(cuisineId), sortby="rating", orderby="desc",limit=100)

		d = json.loads(results)
		response = ""
		if d['results_found'] == 0:
			response = "no results"
		else:
			filtered_rest = self.filter_restaurant_by_budget(
				budget, d['restaurants'])

			print('Length of filtered : ', len(filtered_rest))

			rest_dict = {'Name': [], 'Address': [],
						 'Rating': [], 'Cast for Two': []}
			for rest in filtered_rest:
				rest_dict['Name'].append(rest["restaurant"]["name"])
				rest_dict['Address'].append(
					rest["restaurant"]["location"]["address"])
				rest_dict['Rating'].append(
					rest["restaurant"]["user_rating"]["aggregate_rating"])
				rest_dict['Cast for Two'].append(
					rest["restaurant"]["average_cost_for_two"])

			rest_df = pd.DataFrame.from_dict(rest_dict)

			if(rest_df.shape[0] > 5):
				rest_df = rest_df.head(5).reset_index(drop=True)

			print(rest_df)
			rest_df['Rating'] = rest_df['Rating'].astype(str)
			order = 1
			for index in rest_df.iterrows():
				response = (response + "\n   "
							+ str(order)
							+ ". "
							+ rest_df['Name'][index[0]]
							+ " in "
							+ rest_df['Address'][index[0]]
							+ " has been rated "
							+ rest_df['Rating'][index[0]]
							+ " out of 5"
							+ "\n")
				order += 1

		dispatcher.utter_message("-----"+response)
		global email_payload
		email_payload = """\<html>
  							<head></head>
  							<body>
							{0}
  							</body>
							</html>
							""".format(rest_df.to_html())
		print(email_payload)
		return 

	def filter_restaurant_by_budget(self, budget, restaurant_list):
		print('Length of Unfiltered : ', len(restaurant_list))
		filtered_restaurant_list = []
		rangeMin = 0
		rangeMax = 999999

		if int(budget) <= 299:
			rangeMax = 299
		elif int(budget) >= 300 and int(budget) <= 700:
			rangeMin = 300
			rangeMax = 700
		elif int(budget) >= 701:
			rangeMin = 701
		else:
			rangeMin = 0
			rangeMax = 9999

		for restaurant in restaurant_list:
			avg_cost = int(restaurant["restaurant"]["average_cost_for_two"])

			if avg_cost >= rangeMin and avg_cost <= rangeMax:
				filtered_restaurant_list.append(restaurant)

		return filtered_restaurant_list


class ActionValidateLocation(Action):

	def name(self):
		return "action_validate_location"

	def run(self, dispatcher, tracker, domain):
		location_validity = "valid"
		location = tracker.get_slot("location")

		if not location:
			location_validity = "invalid"
		else:
			filepath = DEFAULT_DATA_PATH + "/validCity.json"

			with open(filepath) as cities_file:

				data = json.load(cities_file)

				if data is not None:
					tier1_cities = data["data"]["tier1"]
					tier2_cities = data["data"]["tier2"]

					tier1_cities_lower = [city.lower()
										  for city in tier1_cities]
					tier2_cities_lower = [city.lower()
										  for city in tier2_cities]

					location_validity = (
						"invalid"
						if location.lower() not in tier1_cities_lower
						and location.lower() not in tier2_cities_lower
						else "valid"
					)
				else:
					location_validity = "invalid"

		return [SlotSet("location_validity", location_validity)]


class ActionValidateCuisine(Action):
	def name(self):
		return "action_validate_cuisine"

	def run(self, dispatcher, tracker, domain):

		cuisine = tracker.get_slot("cuisine")
		cuisine_validity = "valid"

		if not cuisine:
			cuisine_validity = "invalid"
		else:
			supported_cuisines = [
				"american",
				"chinese",
				"italian",
				"mexican",
				"north indian",
				"south indian",
			]

			cuisine_validity = (
				"invalid" if cuisine.lower() not in supported_cuisines else "valid"
			)

		return [SlotSet("cuisine_validity", cuisine_validity)]


class ActionValidateEmail(Action):
	def name(self):
		return "action_validate_email"

	def run(self, dispatcher, tracker, domain):

		email = tracker.get_slot("email")
		email_validity = "valid"

		if not email:
			email_validity = "invalid"
		else:
			regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
			if(re.search(regex, email)):
				email_validity = "valid"

			else:
				email_validity = "invalid"

		return [SlotSet("email_validity", email_validity)]


class ActionSendMail(Action):
	def name(self):
		return "action_send_mail"

	def run(self, dispatcher, tracker, domain):

		email_Id = tracker.get_slot('email')
		email_Payload = email_payload
		print(email_Payload)
		mail_content = '''Hello,
		Here are your requested Top 5 Restaurants ordered by average user ratings.
		
		Thank You'''

		# The mail addresses and password
		sender_address = 'sourav.patel9000@gmail.com'
		sender_pass = ''
		receiver_address = email_Id
		# Setup the MIME
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		# The subject line
		message['Subject'] = 'Here are your requested Top 5 Restaurants :)'
		# The body and the attachments for the mail
		message.attach(MIMEText(mail_content, 'plain'))
		message.attach(MIMEText(email_Payload, 'html'))
		# Create SMTP session for sending the mail
		session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
		session.starttls()  # enable security
		# login with mail_id and password
		session.login(sender_address, sender_pass)
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		print('Mail Sent')


class ActionSlotReset(Action):
	def name(self):
		return 'action_slot_reset'

	def run(self, dispatcher, tracker, domain):
		return[AllSlotsReset()]
