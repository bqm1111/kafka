"""simple consumer"""
import struct
import base64
from json import loads

from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': 'true',
    'group.id': 'mygroup'
})

consumer.subscribe(['C1_example_topic'])

index = 0
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue
    data = loads(msg.value())
    print(f'Received message: {index}: {data}')

consumer.close()