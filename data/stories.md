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

## interactive_story_2
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

## interactive_story_3
* restaurant_search{"avail_mail_service": "send me an email", "cuisine": "italian", "location": "pune", "budget": "600"}
    - slot{"avail_mail_service": "send me an email"}
    - slot{"budget": "600"}
    - slot{"cuisine": "italian"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
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

## interactive_story_4
* restaurant_search{"cuisine": "amurican"}
    - slot{"cuisine": "amurican"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - utter_avail_mail_service
* affirm{"avail_mail_service": "Yes"}
    - slot{"avail_mail_service": "Yes"}
    - utter_ask_email
* restaurant_search{"email": "acb.com"}
    - slot{"email": "acb.com"}
    - action_validate_email
    - slot{"email_validity": "invalid"}
    - utter_email_invalid
    - utter_ask_email_retry
* restaurant_search{"email": "sourav.patel51@gmail.com"}
    - slot{"email": "sourav.patel51@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots
* affirm
    - utter_goodbye

## interactive_story_5
* restaurant_search{"cuisine": "mexican", "location": "oyeoye"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "oyeoye"}
    - action_validate_location
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - utter_avail_mail_service
* affirm{"avail_mail_service": "Yes"}
    - slot{"avail_mail_service": "Yes"}
    - utter_ask_email
* restaurant_search{"email": "sourav.patel51@gmail.com"}
    - slot{"email": "sourav.patel51@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots
* affirm
    - utter_goodbye

## interactive_story_6
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "punjab"}
    - slot{"location": "punjab"}
    - action_validate_location
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
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

## interactive_story_7
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - utter_avail_mail_service
* affirm{"avail_mail_service": "Yes"}
    - slot{"avail_mail_service": "Yes"}
    - utter_ask_email
* restaurant_search{"email": "sourav.patel9000@gmail.com"}
    - slot{"email": "sourav.patel9000@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots
* affirm
    - utter_goodbye

## interactive_story_8
* restaurant_search{"cuisine": "biryani"}
    - slot{"cuisine": "biryani"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - utter_avail_mail_service
* affirm{"avail_mail_service": "Yes"}
    - slot{"avail_mail_service": "Yes"}
    - utter_ask_email
* restaurant_search{"email": "souravpatel51@gmail.com"}
    - slot{"email": "souravpatel51@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots
* affirm
    - utter_goodbye

## interactive_story_9
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "bhubaneswar"}
    - slot{"location": "bhubaneswar"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "No"}
    - slot{"avail_mail_service": "No"}
    - action_slot_reset
    - reset_slots
    - utter_goodbye

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "asansol"}
    - slot{"location": "asansol"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "No"}
    - slot{"avail_mail_service": "No"}
    - action_slot_reset
    - reset_slots
    - utter_goodbye

* restaurant_search{"cuisine": "italian", "location": "Gurgaon"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Gurgaon"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - utter_avail_mail_service
* affirm{"avail_mail_service": "Yes"}
    - slot{"avail_mail_service": "Yes"}
    - utter_ask_email
* restaurant_search{"email": "sourav.patel9000@gmail.com"}
    - slot{"email": "sourav.patel9000@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots
* affirm
    - utter_goodbye

* restaurant_search{"budget": "299", "location": "Mumbai"}
    - slot{"budget": "299"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - utter_avail_mail_service
* affirm{"avail_mail_service": "Yes"}
    - slot{"avail_mail_service": "Yes"}
    - utter_ask_email
* restaurant_search{"email": "sourav.patel9000@gmail.com"}
    - slot{"email": "sourav.patel9000@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots

* restaurant_search{"budget": "701", "cuisine": "italian", "location": "pune"}
    - slot{"budget": "701"}
    - slot{"cuisine": "italian"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
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

* restaurant_search{"budget": "299", "location": "patna"}
    - slot{"budget": "299"}
    - slot{"location": "patna"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "No"}
    - slot{"avail_mail_service": "No"}
    - action_slot_reset
    - reset_slots
    - utter_goodbye

* restaurant_search{"location": "Thiruvananthapuram", "budget": "299"}
    - slot{"budget": "299"}
    - slot{"location": "Thiruvananthapuram"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "No"}
    - slot{"avail_mail_service": "No"}
    - action_slot_reset
    - reset_slots
    - utter_goodbye

* restaurant_search{"budget": "700", "cuisine": "north indian", "location": "Visakhapatnam"}
    - slot{"budget": "700"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Visakhapatnam"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "No"}
    - slot{"avail_mail_service": "No"}
    - action_slot_reset
    - reset_slots
    - utter_goodbye

* restaurant_search{"budget": "299", "location": "Raipur"}
    - slot{"budget": "299"}
    - slot{"location": "Raipur"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "No"}
    - slot{"avail_mail_service": "No"}
    - action_slot_reset
    - reset_slots
    - utter_goodbye
