## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "bhubaneswar"}
    - slot{"location": "bhubaneswar"}
    - action_search_restaurants
    - slot{"location": "bhubaneswar"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"email_payload": "\t\t\t\t\t\t\t\t<html>\n  \t\t\t\t\t\t\t\t<head></head>\n  \t\t\t\t\t\t\t\t<body>\n\t\t\t\t\t\t\t\t<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Name</th>\n      <th>Address</th>\n      <th>Rating</th>\n      <th>Cast for Two</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Domino's Pizza</td>\n      <td>Shop 1 &amp; 4 - 6, Ground Floor, Decision Tower 1, Manjeri, Satara Road, Pune</td>\n      <td>4.1</td>\n      <td>400</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Domino's Pizza</td>\n      <td>Shop 130/24, Ground Floor, Rameera Tower Building, Near Pimpri Chinchwad Town Planning Authority Building, Nigdi, Pune</td>\n      <td>4.0</td>\n      <td>400</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Domino's Pizza</td>\n      <td>Ground Floor, Opposite Bharti Vidyapeeth Gate, Pune Satara Road, Katraj, Pune</td>\n      <td>4.0</td>\n      <td>400</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Domino's Pizza</td>\n      <td>Shop 7, Dhanlaxmi Society, Opposite Jagtap Hospital, Sinhgad Road, Pune</td>\n      <td>4.0</td>\n      <td>400</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Domino's Pizza</td>\n      <td>Fortune Plaza, Near Sayyad Nagar, Hadapsar, Pune</td>\n      <td>4.0</td>\n      <td>400</td>\n    </tr>\n  </tbody>\n</table>\n  \t\t\t\t\t\t\t\t</body>\n\t\t\t\t\t\t\t\t</html>\n\t\t\t\t\t\t\t\t"}
    - utter_avail_mail_service
* affirm{"avail_mail_service": "Yes"}
    - slot{"avail_mail_service": "Yes"}
    - utter_ask_email
* restaurant_search{"email": "sourav.sunil2004@gmail.com"}
    - slot{"email": "sourav.sunil2004@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots
* affirm
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "hyderabad", "budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - slot{"email_payload": "\t\t\t\t\t\t\t\t<html>\n  \t\t\t\t\t\t\t\t<head></head>\n  \t\t\t\t\t\t\t\t<body>\n\t\t\t\t\t\t\t\t<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Name</th>\n      <th>Address</th>\n      <th>Rating</th>\n      <th>Cast for Two</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Kim Fung</td>\n      <td>Opposite NIN Bus Stop, Vijayapuri Colony, Lalaguda Road, Tarnaka, Hyderabad</td>\n      <td>4.2</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Chop Sticks</td>\n      <td>8-3-960/9, Srinagar Colony, Hyderabad</td>\n      <td>4.1</td>\n      <td>300</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Bowl o' China</td>\n      <td>1-8-303/33/A, Nagarm Towers, NTR Circle, S P Road, Secunderabad</td>\n      <td>4.1</td>\n      <td>700</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Alex's Kitchen</td>\n      <td>3-6-10, Liberty Road, Himayath Nagar, Hyderabad</td>\n      <td>4.0</td>\n      <td>600</td>\n    </tr>\n  </tbody>\n</table>\n  \t\t\t\t\t\t\t\t</body>\n\t\t\t\t\t\t\t\t</html>\n\t\t\t\t\t\t\t\t"}
    - utter_avail_mail_service
* affirm{"avail_mail_service": "Yes"}
    - slot{"avail_mail_service": "Yes"}
    - utter_ask_email
* restaurant_search{"email": "sourav.sunil2004@gmail.com"}
    - slot{"email": "sourav.sunil2004@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots
* affirm
    - utter_goodbye
