import sys
from datetime import datetime
from db_repo import DbRepo
from sqlalchemy import asc, text, desc
from sqlalchemy import text
from attraction import Attraction
from tourist import Tourist
from visit import Visit
from db_config import local_session, create_all_entities

repo = DbRepo(local_session)

repo.delete_table('tourists')
repo.delete_table('visits')
repo.delete_table('attractions')

create_all_entities()

t1 = Tourist(name = 'avi', origin_country = 'israel')
t2 = Tourist(name = 'boris', origin_country = 'russia')
a1 = Attraction(name = 'big wheel', price = 300)
a2 = Attraction(name = 'mirror house', price = 400)
a3 = Attraction(name = 'bumper cars', price = 100)
v1 = Visit(tourist_id = 1, attraction_id = 3, year_of_visit = 1990)
v2 = Visit(tourist_id = 1, attraction_id = 1, year_of_visit = 1997)
v3 = Visit(tourist_id = 2, attraction_id = 2, year_of_visit = 2001)
v4 = Visit(tourist_id = 2, attraction_id = 3, year_of_visit = 2020)
repo.add_all([t1, t2, a1, a2, a3, v1, v2, v3, v4])

avi = repo.get_by_condition(Tourist, lambda query: query.filter(Tourist.id == 1).first())
print('*'*50)
print(avi.visits)
print('*'*50)
bigwheel = repo.get_by_condition(Attraction, lambda query: query.filter(Attraction.id == 3).first())
print(bigwheel.visits)
print('*'*50)