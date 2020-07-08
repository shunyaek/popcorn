import pika
import os

user_credentials = {
    "user": os.environ["RABBITMQ_USER"],
    "password": os.environ["RABBITMQ_PASSWORD"],
}


def send(server, queue, user_credentials, message):
    credentials = pika.PlainCredentials(
        user_credentials["user"], user_credentials["password"]
    )
    parameters = pika.ConnectionParameters(server, credentials=credentials)
    connection = pika.BlockingConnection(parameters=parameters)
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange="", routing_key=queue, body=message)
    print("[x] Sent message: '{}'".format(message))
    connection.close()


send("<server_ip/server_name>", "<rabbitmq_queue>", user_credentials, "<message_body>")
