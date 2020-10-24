## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- [Yes](avail_mail_service)
- [Yes](avail_mail_service)

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- yo

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- show me [italian](cuisine) restaurants
- bhubaneswar[]{"entity": "location", "value": "bhubaneswar"}
- [299](budget)
- [700](budget)
- [701](budget)
- [Yes](avail_mail_service)
- [No](avail_mail_service)
- [Sure](avail_mail_service)
- [Nope](avail_mail_service)
- [^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$](email)
- find me restaurant
- [pune](location)
- [sourav.sunil2004@gmail.com](email)
- find me [chinese](cuisine) restaurants in [hyderabad](location) with budget [500](budget)
- can you [send me an email](avail_mail_service) with [italian](cuisine) restaurants in [pune](location) costing around [600](budget)
- find me [amurican](cuisine) restaurants
- i meant [american](cuisine)
- [bangalore]{"entity": "location", "value": "Bengaluru"}
- [acb.com](email)
- [sourav.patel51@gmail.com](email)
- show me [mexican](cuisine) restaurants in [oyeoye](location)
- how about in [bhopal](location)
- find me some [north indian](cuisine) thali
- [punjab](location)
- how about [amritsar](location)
- i'm craving ffor some [south indian](cuisine) food
- [chennai](location)
- [sourav.patel9000@gmail.com](email)
- i'm craving for [chaat](cuisine)
- find me [chaats](cuisine)
- i'm craving for some [biryani](cuisine)
- I'm craving for some [biryani](cuisine)
- how about [arabian](cuisine)
- give me some [north indian](cuisine) then
- [patna](location)
- [souravpatel51@gmail.com](email)
- get me something [mexican](cuisine)
- [bhubaneswar](location)
- find me something [chinese](cuisine)
- [asansol](location)
- find me something [mexican](cuisine) as well
- [allahabad](location)
- find me something [italian](cuisine) in [Gurgaon](location)
- [700](budget)
- [sourav.patel9000@gmail.com](email)

## synonym:4
- four

## synonym:Ahmedabad
- Ahemdabad

## synonym:Bengaluru
- bangalore
- banglore

## synonym:Chennai
- Madras

## synonym:Delhi
- New Delhi
- Delhi NCR
- Dilli

## synonym:Hyderabad
- Hydrabad

## synonym:Kolkata
- Calcutta

## synonym:Mumbai
- Bombay
- Bumbai

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
