from kafka import KafkaConsumer, TopicPartition
from json import loads
import os

OFFSET_FILE = 'consumer_offset.txt'

def save_offset(offset):
    with open(OFFSET_FILE, 'w') as f:
        f.write(str(offset))

def read_offset():
    if os.path.exists(OFFSET_FILE):
        with open(OFFSET_FILE, 'r') as f:
            return int(f.read().strip())
    return None

saved_offset = read_offset()
"""
consumer = KafkaConsumer(
        #'topic1',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=5000,
        #auto_offset_reset="earliest" if saved_offset is None else 'none',
        group_id="fbi", #같은그룹으로 묶고 알려준다.
        enable_auto_commit=False
        )

#consumer_timeout_ms=5000 // 타임아웃 5초 후
#auto_offset_reset=' '    // earliest 이전기록 전부 출력 후 실행, latest 요청 한번만 실행
print("[Start] get consumer")

p = TopicPartition('topic1', 0) # 0 은 파티션 넘버
consumer.assign([p])

if saved_offset is not None:
    consumer.seek(p, saved_offset)
else:
    consumer.seek_to_beginning(p)

for msg in consumer:
    print(f"offset={msg.offset}, value={msg.value}")
    save_offset(msg.offset + 1)
#if msg.value['str'] == 'value9':
    #    print("Exit message received, closing consumer.")
    #    break  # 루프 탈출

print("[End] get consumer")

#consumer.close()
"""

consumer = KafkaConsumer(
    'chat',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='chat-group'
    )
print("채팅 프로그램 - 메시지 수신")
print("메시지 대기 중 ...")

try:
    for msg in consumer:
        print(f"[FRIEND] {msg.value['message']}, 현재시간: {msg.value['time']}")

except KeyboardInterrupt:
    print("채팅 종료")
finally:
    consumer.close()
