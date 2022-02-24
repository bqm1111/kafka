"""simple producer"""
from time import sleep
from json import dumps
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

for e in range(1000):
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    data = {'number': e}
    p.produce('C1_example_topic', dumps(data).encode('utf-8'), callback=delivery_report)
    sleep(5)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()
