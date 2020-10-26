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
    - utter_ask_cuisine
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
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine_retry
    - utter_ask_cuisine
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

* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - utter_avail_mail_service
* affirm{"avail_mail_service": "yes"}
    - slot{"avail_mail_service": "yes"}
    - utter_ask_email
* restaurant_search{"email": "sourav.sunil2004@gmail.com"}
    - slot{"email": "sourav.sunil2004@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "send", "email": "sourav.sunil2004@gmail.com"}
    - slot{"avail_mail_service": "send"}
    - slot{"email": "sourav.sunil2004@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validate_location
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - utter_avail_mail_service
* affirm{"avail_mail_service": "yes"}
    - slot{"avail_mail_service": "yes"}
    - utter_ask_email
* restaurant_search{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots

* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - utter_avail_mail_service
* denial{"avail_mail_service": "no"}
    - slot{"avail_mail_service": "no"}
    - action_slot_reset
    - reset_slots
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "send", "email": "xyz@sth.edu"}
    - slot{"avail_mail_service": "send"}
    - slot{"email": "xyz@sth.edu"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots

* restaurant_search{"avail_mail_service": "send", "budget": "701", "cuisine": "italian", "location": "Delhi", "email": "sourav.patel9000@gmail.com"}
    - slot{"avail_mail_service": "send"}
    - slot{"budget": "701"}
    - slot{"cuisine": "italian"}
    - slot{"email": "sourav.patel9000@gmail.com"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots

* restaurant_search{"budget": "299", "cuisine": "arabian", "location": "leh", "email": "sodd0gmail.com"}
    - slot{"budget": "299"}
    - slot{"cuisine": "arabian"}
    - slot{"email": "sodd0gmail.com"}
    - slot{"location": "leh"}
    - action_validate_location
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - action_validate_email
    - slot{"email_validity": "invalid"}
    - utter_email_invalid
    - utter_ask_email_retry
* restaurant_search{"email": "souravpatel51@gmail.com"}
    - slot{"email": "souravpatel51@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots

* greet
    - utter_greet
* restaurant_search{"budget": "299", "cuisine": "south indian", "krnool": "krnool", "avail_mail_service": "mail", "email": "sourav.ssunil2004@gkll"}
    - slot{"avail_mail_service": "mail"}
    - slot{"budget": "299"}
    - slot{"cuisine": "south indian"}
    - slot{"email": "sourav.ssunil2004@gkll"}
    - action_validate_location
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "kurnool"}
    - slot{"location": "kurnool"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - action_search_restaurants
    - action_validate_email
    - slot{"email_validity": "invalid"}
    - utter_email_invalid
    - utter_ask_email_retry
* restaurant_search{"email": "sourav.sunil2004@gmail.com"}
    - slot{"email": "sourav.sunil2004@gmail.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots
    
* out_of_scope
    - utter_default
* out_of_scope{"out_of_scope": "dream of unicorns"}
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "345665"}
    - slot{"budget": "345665"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "No"}
    - slot{"avail_mail_service": "No"}
    - action_slot_reset
    - reset_slots
    - utter_goodbye

* restaurant_search{"cuisine": "Mangolian"}
    - slot{"cuisine": "Mangolian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "No"}
    - slot{"avail_mail_service": "No"}
    - action_slot_reset
    - reset_slots
    - utter_goodbye

* out_of_scope
    - utter_default
* out_of_scope
    - utter_default
* restaurant_search{"cuisine": "Mangolian"}
    - slot{"cuisine": "Mangolian"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine_retry
* out_of_scope
    - utter_ask_cuisine_retry
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Thrissur"}
    - slot{"location": "Thrissur"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - utter_avail_mail_service
* affirm{"avail_mail_service": "Yes"}
    - slot{"avail_mail_service": "Yes"}
    - utter_ask_email
* restaurant_search{"email": "vinod@enwidth.com"}
    - slot{"email": "vinod@enwidth.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots

* restaurant_search{"cuisine": "south indian", "location": "Chennai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Chennai"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - utter_avail_mail_service
* denial{"avail_mail_service": "no"}
    - slot{"avail_mail_service": "no"}
    - action_slot_reset
    - reset_slots
    - utter_goodbye

* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "send", "email": "vinod@enwidth.com"}
    - slot{"avail_mail_service": "send"}
    - slot{"email": "vinod@enwidth.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots
* affirm
    - utter_goodbye

* restaurant_search{"cuisine": "chinese", "location": "Allahabad"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Allahabad"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants

* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants

* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants

* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location_validity": "valid"}
    - action_validate_cuisine
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "701"}
    - slot{"budget": "701"}
    - action_search_restaurants
    - utter_avail_mail_service
* restaurant_search{"avail_mail_service": "send", "email": "vinod@enwidth.com"}
    - slot{"avail_mail_service": "send"}
    - slot{"email": "vinod@enwidth.com"}
    - action_validate_email
    - slot{"email_validity": "valid"}
    - action_send_mail
    - utter_confirm_email
    - action_slot_reset
    - reset_slots
* affirm
    - utter_goodbye
