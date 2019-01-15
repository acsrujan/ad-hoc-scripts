: "
The script is a quickie to migrate kafka topics. 
#Scenario: I had to migrate several topics from one broker to other broker. However, kafka version I'm using doesn't permit more than one migration at one time. I had to write this quick script because I didn't submit all topics to be migrated in a single json file
"

#!/bin/bash
export ZK_CONN="zk_node_1:2181,zk_node_2:2181,zk_node_3:2181/kafka4"
export VERIFY_QUERY=$(/usr/share/kafka/kafka_2.10-0.9.0.1/bin/kafka-reassign-partitions.sh --zookeeper $ZK_CONN --verify --reassignment-json-file ~/migration.json | grep "completed" | wc -l)
export EXECUTE_QUERY=$(/usr/share/kafka/kafka_2.10-0.9.0.1/bin/kafka-reassign-partitions.sh --zookeeper $ZK_CONN --execute --reassignment-json-file ~/new-migrate.json)
timestamp()
{
 date +"%Y-%m-%d %T"
}
if [ "$VERIFY_QUERY" -eq 2 ];
then
	echo "$(timestamp): executing reassign"; "$EXECUTE_QUERY";
else
	echo "$(timestamp): Not yet";
fi
