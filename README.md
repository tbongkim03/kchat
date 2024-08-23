# kchat

## 0.1.0 create kchat-ping function..

## 0.2.0 create src/kchat/kafka/pro.py & con.py..

- Python chat program using Apache Kafka

```python

# pro.py code ~
data = {'str': 'value' + str(i)}
pro.send('topic1', value=data) 
```

```python

# con.py code ~
value_deserializer=lambda x: loads(x.decode('utf-8'))
consumer_timeout_ms=5000
```

### launch on two terminal tabs

 1. first tab : `$ python src/kchat/kafka/con.py`
    `[Start] get consumer`

 2. second tab : `$ python src/kchat/kafka/pro.py`
    `[DONE]:  0.020064353942871094`

 3. first tab :
```
offset=80, value={'str': 'value0'}
offset=81, value={'str': 'value1'}
offset=82, value={'str': 'value2'}
offset=83, value={'str': 'value3'}
offset=84, value={'str': 'value4'}
offset=85, value={'str': 'value5'}
offset=86, value={'str': 'value6'}
offset=87, value={'str': 'value7'}
offset=88, value={'str': 'value8'}
offset=89, value={'str': 'value9'}
```
 4. first tab :
    ~5 seconds later~
    `[End] get consumer`

### result

`$KAFKA_HOME/bin/kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092`

```json
{"str": "value0"}
{"str": "value1"}
{"str": "value2"}
{"str": "value3"}
{"str": "value4"}
{"str": "value5"}
{"str": "value6"}
{"str": "value7"}
{"str": "value8"}
{"str": "value9"}
```

## 0.3.0 create src/kchat/kafka/chat.py & pchat.py..

- Python chat program using Apache Kafka

```python
# pchat.py code~

data={"message": inp, "time": time.time()}
pro.send('chat', value=data)
```

```python
# chat.py code~

print(f"[FRIEND] {msg.value['message']}, 현재시간: {msg.value['time']}")
```

### result
- first tab
```
$ python src/kchat/kafka/pchat.py

입력: hello
입력: hi
입력: exit
종료합니다.
```

- second tab
```
$ python src/kchat/kafka/chat.py

채팅 프로그램 - 메시지 수신
메시지 대기 중 ...
[FRIEND] hello, 현재시간: 1724228825536
[FRIEND] hi, 현재시간: 1724228845940
[FRIEND] exit, 현재시간: 1724228847115
^C채팅 종료
```

## 0.4.0 create src/kchat/kafka/proAndcon.py & proAndcon2.py..

- Python chat program using Apache Kafka

```python
def pro():
    pass

def con():
    pass

thread_1 = threading.Thread(target = pro)
thread_2 = threading.Thread(target = con)

thread_1.start()
thread_2.start()
```

### result

- first tab
```
python src/kchat/kafka/proAndcon.py
채팅 프로그램
메시지 대기 중 ...
입력: hello
[bong] bong이 나한테 메시지를 보내고있어, 현재시간: 1724298076.7618182
들리나 오바
[bong] 아아아아아ㅏ아, 현재시간: 1724298125.584891
히히히ㅣ히
```

- second tab
```
python src/kchat/kafka/proAndcon.py
채팅 프로그램
메시지 대기 중 ...
입력: [tae] hello, 현재시간: 1724297815.439126
bong이 나한테 메시지를 보내고있어
[tae] 들리나오바, 현재시간: 1724298064.4108975
아아아아아ㅏ아
[tae] 히히히ㅣ히, 현재시간: 1724298123.0562499

```

## 0.5.0 REMAKE src/kchat/kafka/pro.py & con.py..

- Python chat program using Apache Kafka & Docker kafka-ui

### Chages
```python
# pro.py code~

compression_type='gzip'
batch_size=100
```
