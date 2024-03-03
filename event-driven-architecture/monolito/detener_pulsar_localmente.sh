#!/bin/bash
docker compose --profile pulsar down
sudo rm -rf ./data
exit