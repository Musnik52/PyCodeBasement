import pika, sys, os #ייבוא ספריות

def main():
    #חיבור לשרת
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello') #הגדרה של התור

    def callback(ch, method, properties, body): #פונ' להצגת ההודעה שהתקבלה מהיצרן
        print(f" [x] Received: {body.decode()}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt: #תהליך מערכתי לטובת יציאה
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)