import json
import uuid
from facades.facade_anonymus import AnonymusFacade
from tables.users import Users
from tables.flights import Flights
from tables.tickets import Tickets
from tables.customers import Customers
from tables.administrators import Administrators
from tables.airline_companies import AirlineCompanies
from db_files.db_repo import DbRepo
from db_files.db_config import local_session, config
from werkzeug.security import generate_password_hash
from db_files.db_rabbit_consumer import DbRabbitConsumer
from db_files.db_rabbit_producer import DbRabbitProducer

repo = DbRepo(local_session)
anonymus_facade = AnonymusFacade(repo, config)


def customer_callback(ch, method, properties, body):
    #if method POST
    data = json.loads(body)
    new_user = Users(username=data["username"],
                     password=generate_password_hash(data["password"]),
                     email=data["email"],
                     public_id=str(uuid.uuid4()),
                     user_role=config["user_roles"]["customer"])
    new_customer = Customers(first_name=data["first_name"],
                             last_name=data["last_name"],
                             address=data["address"],
                             phone_number=data["phone_number"],
                             credit_card_number=data["credit_card_number"],
                             user_id=new_user.id)
    anonymus_facade.add_customer(new_customer, new_user)
    rabbit_producer = DbRabbitProducer(data["queue_name"])
    rabbit_producer.publish(json.dumps(
        {"status": "SUCCESS", "name": data["first_name"], "user": data["username"]}))


def main():
    customer_rabbit = DbRabbitConsumer(
        queue_name='createCustomer', callback=customer_callback)
    customer_rabbit.consume()


if __name__ == '__main__':
    main()
