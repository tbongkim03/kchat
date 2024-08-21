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
    
    `ConsumerRecord(topic='topic1', partition=0, offset=80, timestamp=1724211818595, timestamp_type=0, key=None, value={'str': 'value0'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
ConsumerRecord(topic='topic1', partition=0, offset=81, timestamp=1724211818598, timestamp_type=0, key=None, value={'str': 'value1'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
ConsumerRecord(topic='topic1', partition=0, offset=82, timestamp=1724211818600, timestamp_type=0, key=None, value={'str': 'value2'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
ConsumerRecord(topic='topic1', partition=0, offset=83, timestamp=1724211818602, timestamp_type=0, key=None, value={'str': 'value3'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
ConsumerRecord(topic='topic1', partition=0, offset=84, timestamp=1724211818609, timestamp_type=0, key=None, value={'str': 'value4'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
ConsumerRecord(topic='topic1', partition=0, offset=85, timestamp=1724211818611, timestamp_type=0, key=None, value={'str': 'value5'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
ConsumerRecord(topic='topic1', partition=0, offset=86, timestamp=1724211818613, timestamp_type=0, key=None, value={'str': 'value6'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
ConsumerRecord(topic='topic1', partition=0, offset=87, timestamp=1724211818615, timestamp_type=0, key=None, value={'str': 'value7'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
ConsumerRecord(topic='topic1', partition=0, offset=88, timestamp=1724211818617, timestamp_type=0, key=None, value={'str': 'value8'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
ConsumerRecord(topic='topic1', partition=0, offset=89, timestamp=1724211818619, timestamp_type=0, key=None, value={'str': 'value9'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)`

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
