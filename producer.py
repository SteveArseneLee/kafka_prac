import time
from kafka import KafkaProducer
from faker import Faker

producer = KafkaProducer(bootstrap_servers=['localhost:9092,localhost:9093,localhost:9094'])
for _ in range(100):
    name = Faker.name()
    producer.send('names', name.encode('utf-8'))
    print(name)
time.sleep(20)