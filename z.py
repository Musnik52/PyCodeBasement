import requests
import json

#from WEBSITE
for i in range(10):
    response = requests.get("https://randomuser.me/api")
    print(f"{response.json()['results'][0]['login']['username']}")
    print(f"{response.json()['results'][0]['login']['password']}")
    print(f"{response.json()['results'][0]['name']['first']}")
    print(f"{response.json()['results'][0]['name']['last']}")
    print(f"{response.json()['results'][0]['location']['street']['name']}")
    print(f"{response.json()['results'][0]['location']['street']['number']}")
    print(f"{response.json()['results'][0]['email']}")
    print(f"{response.json()['results'][0]['phone']}")

#from JSON file
countries = open('C:\git\pyCodeBasement\FINAL_PROJECT\countries.json')
data = json.load(countries)
for i in data:
    print(i['name'])
countries.close()