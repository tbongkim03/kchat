from kafka import KafkaProducer
import time
import json
from tqdm import tqdm

pro = KafkaProducer(
        bootstrap_servers=['172.17.0.1:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8'),
        compression_type='gzip',
        batch_size=100
        )

start = time.time()
for i in tqdm(range(10000)):
    data = {'str': 'value' + str(i)}
    pro.send('test-gzip100', value=data)
    pro.flush()
    time.sleep(0.001)
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
