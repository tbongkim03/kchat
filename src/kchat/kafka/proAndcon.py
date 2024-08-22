from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import json
from json import loads
import time
import os

# 테스트
import threading

def pro():
    pro = KafkaProducer(
            bootstrap_servers=['ec2-3-39-223-117.ap-northeast-2.compute.amazonaws.com:9092'],
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
            )

    print("채팅 프로그램")
    print("메시지 대기 중 ...")

    while True:
        inp=input("입력: ")
        data={"message": inp, "time": time.time()}
        pro.send('tae', value=data)
        pro.flush()

        if inp == 'exit':
            print('종료합니다.')
            break

def con():
    consumer = KafkaConsumer(
        'bong',
        bootstrap_servers=['ec2-3-39-223-117.ap-northeast-2.compute.amazonaws.com:9092'],
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        auto_offset_reset='lastest',
        enable_auto_commit=True,
        group_id='chat-group'
        )

    while True:
        try:
            for msg in consumer:
                print(f"[{msg.topic}] {msg.value['message']}, 현재시간: {msg.value['time']}")
        except KeyboardInterrupt:
            print("채팅 종료")
        finally:
            consumer.close()

thread_1 = threading.Thread(target = pro)
thread_2 = threading.Thread(target = con)

thread_1.start()
thread_2.start()

"""

# PRO CODE
while True:
    print("채팅 프로그램")
    print("메시지 대기 중 ...")
    
    inp=input("입력: ")
    data={"message": inp, "time": time.time()}
    pro.send('태', value=data)
    pro.flush()
    for msg in consumer:
        print(f"[{msg.topic}] {msg.value['message']}, 현재시간: {msg.value['time']}"
    if inp == 'exit':
        print('종료합니다.')
        break


# CON CODE

try:
    for msg in consumer:
        print(f"[{msg.topic}] {msg.value['message']}, 현재시간: {msg.value['time']}"

except KeyboardInterrupt:
    print("채팅 종료")
finally:
    consumer.close()

"""
