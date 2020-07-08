import pika
import os

user_credentials = {
    "user": os.environ["RABBITMQ_USER"],
    "password": os.environ["RABBITMQ_PASSWORD"],
}


def receive(server, queue, user_credentials):
    credentials = pika.PlainCredentials(
        user_credentials["user"], user_credentials["password"]
    )
    parameters = pika.ConnectionParameters(server, credentials=credentials)
    connection = pika.BlockingConnection(parameters=parameters)
    channel = connection.channel()
    channel.queue_declare(queue=queue)

    def callback(ch, method, properties, body):
        print(" [x] Received: '{}'".format(body))

    channel.basic_consume(queue=queue, auto_ack=True, on_message_callback=callback)
    print(" [*] Waiting for messages. To exit press CTRL + C")
    channel.start_consuming()


receive("<server_ip/server_name>", "<rabbitmq_queue>", user_credentials)
