# Jeremiah Gallagher
# CSIS-354
# Message Queueing with RabbitMQ

# send.py
import pika
import time
# establish connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# create a hello queue to which the message will be delivered
channel.queue_declare(queue='hello')

# create a counter to track the number of messages sent/ update the message number
counter = 1

# embed the message into a loop that sends the message, updates the counter and delays 1 second before repeating.
while True:
    channel.basic_publish(exchange='', routing_key='hello', body='Hello! My name is Jeremiah. Python is awesome! ' +
                                                                 str(counter))
    print("[x] sent message.")    # print local message to verify a message was sent
    counter += 1                        # update counter
    time.sleep(1)                       # delay 1 second

connection.close()


