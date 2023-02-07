import pika

parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.confirm_delivery()
