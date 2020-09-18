# Jeremiah Gallagher
# CSIS-354
# Message Queueing with RabbitMQ

# receive.py
import pika
# establish connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# create a hello queue to which the message will be delivered
channel.queue_declare(queue='hello')


# print the received message out to the console
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# tell RabbitMQ that this particular callback function should receive messages from our hello queue:
channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

# enter a never-ending loop that waits for data and runs callbacks whenever necessary
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
