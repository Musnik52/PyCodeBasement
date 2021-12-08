from datetime import datetime
from user import User
from car import Car
from sqlalchemy import text
from db_config import local_session, create_all_entities

# create tables
create_all_entities()

# local_session.add(User(username='bob', email='bob@bob.com'))
# local_session.commit()

# add a list of users and a list of cars
users_list = [User(username='rob', email='rob@rob.com'), User(username='job', email='job@job.com')]
cars_list = [Car(model='fiesta', brand='ford'), Car(model='civic', brand='honda')]
local_session.add_all(users_list)
local_session.add_all(cars_list)
local_session.commit()

# delete a user and a car
local_session.query(User).filter(User.id == 2).delete(synchronize_session=False)
local_session.query(Car).filter(Car.id == 2).delete(synchronize_session=False)
local_session.commit()

# print all users and all cars
users = local_session.query(User).all()
cars = local_session.query(Car).all()
print(users)
print(cars)
'''
# add a list of cars
cars_list = [Car(model='fiesta', brand='ford'), Car(model='civic', brand='honda')]
local_session.add_all(cars_list)
local_session.commit()

# delete a car
local_session.query(Car).filter(Car.id == 2).delete(synchronize_session=False)
local_session.commit()

# print all cars
cars = local_session.query(Car).all()
print(cars)
'''