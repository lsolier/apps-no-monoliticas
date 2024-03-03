#!/bin/bash
mkdir -p data/bookkeeper
mkdir -p data/zookeeper
sudo chmod -R 777 ./data
docker compose --profile pulsar up

exit