# Kafka setup

## TODO

- [x] Single kafka server
  - [x] Basic kafka server
  - [x] GUI for easy inspect the server 
- [ ] Setup activate-activate multi cluster
  - [ ] Setup 2 cluster of kafka (each has 2 network interfaces)
- [ ] Example client
  - [x] Python
  - [ ] C/C++
  - [ ] Javascript

## Start

```bash
docker-compose -p cluster1 up -d
```

## Configuration notes

## References

- <https://www.altoros.com/blog/multi-cluster-deployment-options-for-apache-kafka-pros-and-cons/>
- <https://docs.confluent.io/platform/current/multi-dc-deployments/replicator/replicator-docker-tutorial.html#replicator>