import random
import json
import requests
from db_repo import DbRepo
from db_config import connection_string, config
from db_gen_base import DbRepoConnectionPool
from tables.users import Users
from tables.customers import Customers
from tables.countries import Countries

class DbGenerator(DbRepoConnectionPool):

    def __init__(self):
        super().__init__()
        self.repo = DbRepo(connection_string)
        self.response = requests.get(config["db"]["api"])

    '''async def get_data(self):
        async with httpx.AsyncClient() as client:
            r = await client.get(self.response)
            return r.json()'''

    def create_user(self, user_role):
        inserted_user = Users(  username = self.response.json()['results'][0]['login']['username'], 
                                password = self.response.json()['results'][0]['login']['password'], 
                                email = self.response.json()['results'][0]['email'], 
                                user_role = user_role)
        self.repo.add(inserted_user)
        return inserted_user.id

    def create_customers(self, num):
        for l in range(num):
            credit_card_number = str(random.randint(0, 9))
            for i in range(11): credit_card_number = credit_card_number + str(random.randint(0, 9))
            user_id = self.create_user(config["user_roles"]["customer"])
            new_customer = Customers(first_name = self.response.json()['results'][0]['name']['first'],
                                    last_name = self.response.json()['results'][0]['name']['last'],
                                    address = str(self.response.json()['results'][0]['location']['street']['name']+' '+self.response.json()['results'][0]['location']['street']['number']), 
                                    phone_number = self.response.json()['results'][0]['phone'],
                                    credit_card_number = credit_card_number,
                                    user_id = user_id)
            self.repo.add(new_customer)

    def create_countries(self):
        countries_ls = []
        with open(config["db"]["countries_json"]) as f: countries = json.load(f)
        #for i in range(num):
        for country in countries: countries_ls.append(Countries(name=country['name']))
        self.repo.add_all(countries_ls)
