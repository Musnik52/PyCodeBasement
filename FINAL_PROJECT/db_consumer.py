import json
import uuid
import pika
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

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')


def fib(data):
    if data == 0:
        return 0
    elif data == 1:
        return 1
    else:
        return fib(data - 1) + fib(data - 2)


def on_request(ch, method, props, body):
    data = int(body)
    print(ch, method, props, body)

    print(f" [.] Data Received({data})")
    response = fib(data)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()

# def customer_callback(ch, method, properties, body):
#     data = json.loads(body)
#     if data["action"] == 'add':
#         new_user = Users(username=data["username"],
#                          password=generate_password_hash(data["password"]),
#                          email=data["email"],
#                          public_id=str(uuid.uuid4()),
#                          user_role=config["user_roles"]["customer"])
#         new_customer = Customers(first_name=data["first_name"],
#                                  last_name=data["last_name"],
#                                  address=data["address"],
#                                  phone_number=data["phone_number"],
#                                  credit_card_number=data["credit_card_number"],
#                                  user_id=new_user.id)
#         anonymus_facade.add_customer(new_customer, new_user)
#     elif data["action"] == "update":
#         customer_facade = anonymus_facade.login('qwertytre', '123456789')
#         customer_id = int(data["id"])
#         customer_updates = {"first_name": data["first_name"],
#                             "last_name": data["last_name"],
#                             "address": data["address"],
#                             "phone_number": data["phone_number"],
#                             "credit_card_number": data["credit_card_number"]}
#         customer_facade.update_customer(customer_updates, customer_id)
#     elif data["action"] == "remove":
#         pass

#     rabbit_producer = DbRabbitProducer(data["queue_name"])
#     rabbit_producer.publish(json.dumps({"status": "SUCCESS"}))


# if __name__ == '__main__':
#     customer_rabbit = DbRabbitConsumer(
#         queue_name='customer', callback=customer_callback)
#     customer_rabbit.consume()
