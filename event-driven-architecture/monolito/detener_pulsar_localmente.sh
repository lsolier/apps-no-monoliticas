#!/bin/bash
docker compose --profile pulsar down
sudo rm -rf ./data/bookkeeper
sudo rm -rf ./data/zookeeper
exit