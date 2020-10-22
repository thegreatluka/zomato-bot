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

## interactive_story_1
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

## interactive_story_1
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
    - slot{"email_payload": "\t\t\t\t\t\t\t\t<html>\n  \t\t\t\t\t\t\t\t<head></head>\n  \t\t\t\t\t\t\t\t<body>\n\t\t\t\t\t\t\t\t<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Name</th>\n      <th>Address</th>\n      <th>Rating</th>\n      <th>Cast for Two</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Domino's Pizza</td>\n      <td>Shop 1 &amp; 4 - 6, Ground Floor, Decision Tower 1, Manjeri, Satara Road, Pune</td>\n      <td>4.1</td>\n      <td>400</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Domino's Pizza</td>\n      <td>Shop 130/24, Ground Floor, Rameera Tower Building, Near Pimpri Chinchwad Town Planning Authority Building, Nigdi, Pune</td>\n      <td>4.0</td>\n      <td>400</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Domino's Pizza</td>\n      <td>Ground Floor, Opposite Bharti Vidyapeeth Gate, Pune Satara Road, Katraj, Pune</td>\n      <td>4.0</td>\n      <td>400</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Domino's Pizza</td>\n      <td>Shop 7, Dhanlaxmi Society, Opposite Jagtap Hospital, Sinhgad Road, Pune</td>\n      <td>4.0</td>\n      <td>400</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Domino's Pizza</td>\n      <td>Fortune Plaza, Near Sayyad Nagar, Hadapsar, Pune</td>\n      <td>4.0</td>\n      <td>400</td>\n    </tr>\n  </tbody>\n</table>\n  \t\t\t\t\t\t\t\t</body>\n\t\t\t\t\t\t\t\t</html>\n\t\t\t\t\t\t\t\t"}
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

## interactive_story_1
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
    - slot{"email_payload": "\t\t\t\t\t\t\t\t<html>\n  \t\t\t\t\t\t\t\t<head></head>\n  \t\t\t\t\t\t\t\t<body>\n\t\t\t\t\t\t\t\t<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Name</th>\n      <th>Address</th>\n      <th>Rating</th>\n      <th>Cast for Two</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Leon Grill</td>\n      <td>1671, 9th Main, 4th Cross, HAL 3rd Stage, Jeevan Bhima Nagar, Bangalore</td>\n      <td>4.4</td>\n      <td>600</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Leon Grill</td>\n      <td>123, KHB 1st Cross Road, Koramangala 5th Block, Bangalore</td>\n      <td>4.3</td>\n      <td>600</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Wolf'ish</td>\n      <td>1A, Church Street, Bangalore</td>\n      <td>4.2</td>\n      <td>700</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Leon Grill</td>\n      <td>2117/25, 4th Cross, 2nd Stage, HRBR Layout, Kalyan Nagar, Bangalore</td>\n      <td>4.2</td>\n      <td>600</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Leon Grill</td>\n      <td>Ground Floor, House of Lords, Sampangi Rama Nagar, St. Marks Road, Bangalore</td>\n      <td>4.2</td>\n      <td>600</td>\n    </tr>\n  </tbody>\n</table>\n  \t\t\t\t\t\t\t\t</body>\n\t\t\t\t\t\t\t\t</html>\n\t\t\t\t\t\t\t\t"}
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

## interactive_story_1
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
    - slot{"email_payload": "\t\t\t\t\t\t\t\t<html>\n  \t\t\t\t\t\t\t\t<head></head>\n  \t\t\t\t\t\t\t\t<body>\n\t\t\t\t\t\t\t\t<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Name</th>\n      <th>Address</th>\n      <th>Rating</th>\n      <th>Cast for Two</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Total Refreshing Point</td>\n      <td>Campion School Shahpura, Bhopal, Arera Colony, Bhopal</td>\n      <td>3.8</td>\n      <td>200</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Hotel Atishay</td>\n      <td>Mezzanine Floor, R 55, Zone 1, Maharana Pratap Nagar, Bhopal</td>\n      <td>3.8</td>\n      <td>200</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Mr. Petu</td>\n      <td>Shop no. 7 , hawkers corner 6 no. Bus stop shivaji nagar bhopal</td>\n      <td>3.5</td>\n      <td>200</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Desi Fusion By Firangi Cafe</td>\n      <td>Shop 3, 35 Zone-2, MP Nagar, Bhopal, Maharana Pratap Nagar, Bhopal</td>\n      <td>0.0</td>\n      <td>250</td>\n    </tr>\n  </tbody>\n</table>\n  \t\t\t\t\t\t\t\t</body>\n\t\t\t\t\t\t\t\t</html>\n\t\t\t\t\t\t\t\t"}
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
