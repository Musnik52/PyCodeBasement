from db_rabbit_consumer import DbRabbitConsumer
from db_data_object import DbDataObject
import json

def main():
    rabbit = DbRabbitConsumer(queue_name='DataToGenerate', callback=callback)
    rabbit.consume()

def callback(ch, method, properties, body):
    data = json.loads(body)
    airlines = int(data['airlines'])
    customers = int(data['customers'])
    flights_per_airline = int(data['flights_per_airline'])
    tickets_per_customer = int(data['tickets_per_customer'])
    db_data = DbDataObject( airlines=airlines,
                            customers=customers,
                            flights_per_airline=flights_per_airline,
                            tickets_per_customer=tickets_per_customer)
    db_data.generate_data()

if __name__ == '__main__': main()