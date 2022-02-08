import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
k = 0
inp = None
while inp != 0:
    inp = int(input('Enter a number: '))
    k += inp
    channel.basic_publish(exchange='', routing_key='hello',  body=f"{inp}")
    channel.basic_publish(exchange='', routing_key='hello',  body=f"Boris' input sum is {k}")

print("END OF TRANSMITION'")