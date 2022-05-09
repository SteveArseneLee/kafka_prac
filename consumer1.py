from kafka import KafkaConsumer
from json import loads

# topic, broker list
consumer = KafkaConsumer(
    'test',
    bootstrap_servers=['localhost:9092'],
    auto_offset_rest='earlist',
    enable_auto_commit=True,
    group_id='my-group',
    value_serializer=lambda x: loads(x.decode('utf-8')),
    # consumer_timeout_ms=1000
)

# consumer list 가져오기
print('[begin] get consumer list')
for message in consumer:
    print("Topic: %s, Partition: %d, offset: %d, Key: %s, Value: %s" %(
        message.topic, message.partition, message.offset, message.key, message.value
    ))
print('[end] get consumer list')