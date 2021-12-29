import sys
from datetime import datetime
from user import User
from dbrepo import DbRepo
from sqlalchemy import asc, text, desc
from company import Company
from db_config import local_session, create_all_entities

# create tables
create_all_entities()

repo = DbRepo(local_session)

#get_all
print(users := repo.get_all(User))
print(companies := repo.get_all_limit(Company, 3))

#get_all_asc/desc
print('asc', users := repo.get_all_order_by(User, User.username, asc))
print('desc', users := repo.get_all_order_by(User, User.username, desc))
print('asc', companies := repo.get_all_order_by(Company, Company.name, asc))
print('desc', companies := repo.get_all_order_by(Company, Company.name, desc))

#Insert
repo.add(moshe := User(username='moshe', email='moshe@jb.com'))
repo.add_all(users_list := [User(username='sivan', email='sivan@jb.com'), User(username='shachar', email='shachar@jb.com')] )
repo.add(bioboris := Company(name='bioboris', age=3, address='rashi 31', salary=69000))
repo.add_all(users_list := [musnitech := Company(name='musnitech', age=10, address='here 31', salary=42000), boricosmetix := Company(name='boricosmetix', age=17, address="there 31", salary=66600)])

#delete
repo.delete_by_id(User, User.id, 2)
repo.delete_by_id(Company, Company.id, 2)

#update
repo.update_by_id(User, User.id, 3,{'username': 'shawshaw'}) #update({User.username: 'new moshe', 'email':'moshe@walla.com'}, synchronize_session=False)
repo.update_by_id(Company, Company.id, 3,{'name': 'borincasmetics', 'address': 'somewhere 31'})

#get_by_colname
repo.get_by_column_value