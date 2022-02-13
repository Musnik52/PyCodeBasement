import requests
for i in range(10):
    response = requests.get("https://randomuser.me/api")
    print(f"{response.json()['results'][0]['login']['username']} {response.json()['results'][0]['login']['password']}")