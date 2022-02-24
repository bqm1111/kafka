# Python client example

## Usage

First create a topic with ` create_topic.py`.  

Then, open 2 terminals. The first runs `python simple_producer.py`, the second runs `python simple_consumer.py`. You can see that data is sent from `producer -> server -> consumer`

## Notes

- The Pypi package `kafka-python==2.0.2` has some bug, use [confluent-kafka-python](https://github.com/confluentinc/confluent-kafka-python) instead
- Python code are from <https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1>