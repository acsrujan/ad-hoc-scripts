# ad-hoc-scripts
A bunch of ad-hoc scripts which I often use at work.


### kafka-migrate.sh

Scenario: I had to migrate some topic/partitions from one broker to other broker. I should've created all the topics in a single json file and execute the command. However, I made a mistake in one of the partitions and had to let the current migration complete before i start other one. So, this is just a quick if else script to do it automatically and I've added it to cron job.


### 
