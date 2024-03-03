#!/bin/bash
mkdir -p data/mysql
sudo chmod -R 777 ./data
sudo chmod -R 777 ./connectors
docker compose --profile db up

exit