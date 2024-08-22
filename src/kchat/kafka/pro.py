from kafka import KafkaProducer
import time
import json

pro = KafkaProducer(
        bootstrap_servers=['ec2-3-39-223-117.ap-northeast-2.compute.amazonaws.com:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8'))

start = time.time()
for i in range(10):
    data = {'str': 'Hello' + str(i)}
    pro.send('topic1', value=data)
    pro.flush()
end = time.time()
print('[DONE]: ', end - start)

"""
def kchat_p():
    pro = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

    #start = time.time()
    while True:
        inp=input("입력: ")
        data={"message": inp}
        pro.send('chat', value=data)
        pro.flush()
        if inp == 'exit':
            print('종료합니다.')
            break
    #end = time.time()
"""
