### Elasticsearch quick reference API commands, to be run in client, for health checks, maintenance, etc.

1. Quick health check
`curl -XGET client.elasticsearch.vpc:9200/_cat/health?v`

2. Quick node check
`curl -XGET client.elasticsearch.vpc:9200/_cat/nodes?v`

3. Quick allocation check
`curl -XGET client.elasticsearch.vpc:9200/_cat/allocation?v`

4. To stop allocation temporarily:
`curl -XPUT client.elasticsearch.vpc:9200/_cluster/settings -d '{"transient":{"cluster.routing.allocation.enable":"none"}}'`

To re-enable: 
`curl -XPUT client.elasticsearch.vpc:9200/_cluster/settings -d '{"transient":{"cluster.routing.allocation.enable":"all"}}'`

5. To exclude an IP address:

`curl -XPUT client.elasticsearch.vpc:9200/_cluster/settings -H 'Content-Type: application/json' -d '{"transient" :{"cluster.routing.allocation.exclude._ip" : "x.x.x.x"}}'`

6. To find out which allocations are in progress:
`curl -XGET client.elasticsearch.vpc:9200/_cat/recovery?active_only=true?v`
