from kafka import KafkaProducer
import time
import json

pro = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

#start = time.time()
    
while True:
    inp=input("입력: ")
    data={"message": inp, "time": time.time()}
    pro.send('chat', value=data)
    pro.flush()
    if inp == 'exit':
        print('종료합니다.')
        break
#end = time.time()
