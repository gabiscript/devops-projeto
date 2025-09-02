#!/bin/bash

docker pull gabrielamds/devops-api:latest
docker pull nginx:latest

docker-compose down     
docker-compose up -d     

echo "Deploy via docker-compose finalizado! API e Nginx rodando"
