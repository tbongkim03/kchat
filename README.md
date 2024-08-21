# kchat

## 0.1.0 create kchat-ping function..

## 0.2.0 create src/kchat/kafka/pro.py..

```python
data = {'str': 'value' + str(i)}
pro.send('topic1', value=data) 
```

### launch

`$ Python src/kchat/kafka/pro.py`

### result
`$ KAFKA_HOME/bin/kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092`

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
