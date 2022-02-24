"""create topic"""
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import KafkaException

admin_client = AdminClient({
    'bootstrap.servers': 'localhost:9092',
})

topic_list = []
topic_list.append(NewTopic(topic="C1_example_topic", num_partitions=1, replication_factor=1))

# validate before doing anything
try:
    admin_client.create_topics(new_topics=topic_list, validate_only=True)
except KafkaException:
    import sys
    sys.exit(1)

# now create the topic actually
topic_creation_results = admin_client.create_topics(new_topics=topic_list, validate_only=True)

# Wait for each operation to finish.
for topic, f in topic_creation_results.items():
    try:
        f.result()  # The result itself is None
        print(f"Topic {topic} created")
    except KafkaException as e:
        print(f"Failed to create topic {topic}: {e}")

