Operations on kafka for self guidance:

1. Describe config for a topic:

`bin/kafka-configs.sh --zookeeper localhost:2181 --describe --entity-type topics --entity-name sample_topic`

2. Describe topic:

`bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic sample_topic` 

To describe all topics, replace `--topic sample_topic` by `all`

3. Change retention period for a topic:
`bin/kafka-configs.sh --zookeeper localhost:2181 --alter --entity-type topics --entity-name sample_topic --add-config retention.ms=86400000`

4. 
