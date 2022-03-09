import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
inp = None
while inp != 0:
    inp = int(input('Enter a number: '))
    channel.basic_publish(exchange='', routing_key='hello',  body=f'{inp}')

print("END OF TRANSMIION'")