import json
import random
import sys
from datetime import datetime, timedelta
from time import sleep

from kafka import KafkaProducer

SERVER = "broker:9092"
TOPIC = "streaming"

if __name__ == "__main__":
    
    
    producer = KafkaProducer(
        bootstrap_servers=[SERVER],
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )
    
    try:
        while True:
            
            message = {
                # TWOJ KOD TUTAJ
            }
            producer.send(TOPIC, value=message)
            sleep(1)
    except KeyboardInterrupt:
        producer.close()
