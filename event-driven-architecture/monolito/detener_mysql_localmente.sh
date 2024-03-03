#!/bin/bash
docker compose --profile db down
sudo rm -rf ./data/mysql
exit