# ad-hoc-scripts, cheat sheets, quick commands
A bunch of ad-hoc scripts which I often use at work. This repo is mostly for self reference because I've a super human brain that forgets what.. oops!


### kafka-migrate.sh

Scenario: I had to migrate some topic/partitions from one broker to other broker. I should've created all the topics in a single json file and execute the command. However, I made a mistake in one of the partitions and had to let the current migration complete before i start other one. So, this is just a quick if else script to do it automatically and I've added it to cron job.


### kafka-ops.md

A quick personal cheatsheet of kafka ops.

### Elasticsearch-cheatsheet.md

A quick personal cheatsheet of elasticsearch commands.
