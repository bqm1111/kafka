"""create topic"""
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import KafkaException
admin_client = AdminClient({
    'bootstrap.servers': '172.21.100.167:9092',
})

config_topic1 = {
          'segment.bytes': 1800000000, #1.8GB
          'retention.ms': 600000, # 10 minutes'
          'max.message.bytes': 20970880 # 20MB
          }

config_topic100 = {
          'segment.bytes': 1073741824, #1GB 
          'retention.ms': 1200000, # 20 minutes'
          'max.message.bytes': 20970880 # 20MB
          }

config_topic101 = {
          'segment.bytes': 1073741824, #1GB 
          'retention.ms': 1200000, # 20 minutes'
          'max.message.bytes': 20970880 # 20MB
          }

topic_list = []
topic_list.append(NewTopic(topic="RawMeta_300MB_10m", num_partitions=1, replication_factor=1, config=config_topic1))
topic_list.append(NewTopic(topic="RawImage_30MB_20m", num_partitions=1, replication_factor=1, config=config_topic100))
topic_list.append(NewTopic(topic="Display_30MB_20m", num_partitions=1, replication_factor=1, config=config_topic101))

# validate before doing anything
# try:
#     admin_client.create_topics(new_topics=topic_list, validate_only=True)
# except KafkaException:
#     import sys
#     sys.exit(1)

fs = admin_client.create_topics(topic_list)
# Wait for each operation to finish.
for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))