import pika #ייבוא ספריה

#ייצור החיבור לשרת
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello') #הגדרת התור הרצוי

inp = None
while inp != 0:
    inp = int(input('Enter a number: '))
    channel.basic_publish(exchange='', routing_key='hello',  body=f'{inp}')
    #שליחת מספרים שהם לא 0 אל צרכן, בצירוף סיווג עם מפתח

print("END OF TRANSMIION'")