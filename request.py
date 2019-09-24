import requests
import json
URL = "http://127.0.0.1:5000/"

data = {'club_name': "Arun Fan Club", 'username':'jerry1ye10'}
requests.post(url = URL + "api/favorite", data = data)

data2 = {'update': False, 'name': "Jerry Fan Club", 'description': 'Jerry is cool!', 'tags': 'fans,cool'} #Tags parameter must be sent as a string of commas
requests.post(url = URL + "api/clubs", data = data2)

data3 = {'update': True, 'name': "Jerry Fan Club", 'description': 'Jerry is really cool!', 'tags': 'fans,cool'} #Tags parameter must be sent as a string of commas
requests.post(url = URL + "api/clubs", data = data3)

data4 = {'username': "jerry1ye10", 'event_name': 'PennLabs Application', 'event_description': 'Hard but fun project!', 'location' : 'UPenn', 'time':'September, 23rd, 2019'} #Tags parameter must be sent as a string of commas
requests.post(url = URL + "api/event", data = data4)
