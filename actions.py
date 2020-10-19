from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, AllSlotsReset
import zomatopy
import json

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
			"", lat, lon, str(cuisineId), 5)

		d = json.loads(results)
		response = ""
		if d['results_found'] == 0:
			response = "no results"
		else:
			filtered_rest = self.filter_restaurant_by_budget(
				budget, d['restaurants'])

			print('Length of filtered : ',len(filtered_rest))
			
			for index in range(0, len(filtered_rest)):
				restaurant = filtered_rest[index]
				response = (response + "\n   "
							+ str(index + 1)
							+ ". "
							+ restaurant["restaurant"]["name"]
							+ " in "
							+ restaurant["restaurant"]["location"]["address"]
							+ " has been rated "
							+ restaurant["restaurant"]["user_rating"]["aggregate_rating"]
							+ " out of 5"
							+ "\n")

		dispatcher.utter_message("-----"+response)
		return [SlotSet('location', loc)]

	def filter_restaurant_by_budget(self, budget, restaurant_list):
		filtered_restaurant_list = []
		rangeMin = 0
		rangeMax = 999999

		if budget == "299":
			rangeMax = 299
		elif budget == "700":
			rangeMin = 300
			rangeMax = 700
		elif budget == "701":
			rangeMin = 701
		else:
			rangeMin = 0
			rangeMax = 9999

		for restaurant in restaurant_list:
			print(restaurant)
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


class ActionSlotReset(Action):
	def name(self):
		return 'action_slot_reset'

	def run(self, dispatcher, tracker, domain):
		return[AllSlotsReset()]
