# Automated Web Application Deployment on AWS

## Tech Stack
- AWS EC2, VPC, Security Groups
- Docker
- Python & Bash
- GitHub Actions

## Features
- Simple Flask web app
- Dockerized deployment
- GitHub CI/CD pipeline to EC2 on push
- Secure infra setup with SSH keys and isolated VPC

## Deployment
Push to `main` branch triggers:
1. SSH to EC2
2. Pull latest code
3. Build and run Docker container
