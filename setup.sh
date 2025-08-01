#!/bin/bash

sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker $USER

cd aws-deploy-app
docker build -t flask-app .
docker run -d -p 80:5000 flask-app
