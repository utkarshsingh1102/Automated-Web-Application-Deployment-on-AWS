📦 Automated Web Application Deployment on AWS
This project demonstrates how to automate the deployment of a simple Flask-based web application on an AWS EC2 instance using Docker and GitHub Actions. It features a complete CI/CD pipeline that builds and deploys the app automatically upon every push to the main branch.

🔧 Tech Stack
  AWS (EC2, VPC, Security Groups)
  Docker
  Python / Bash Scripting
  GitHub Actions

🚀 Features
  Flask-based web app containerized with Docker
  Automated deployment to EC2 using GitHub Actions
  Custom Bash & Python scripts for setup and redeployment
  Secure networking using AWS VPC & Security Groups

📂 Project Structure
  app/: Flask web application
  Dockerfile: Docker setup for the app
  setup.sh: Bash script for EC2 environment setup
  deploy.py: Python script for redeployment
  .github/workflows/: GitHub Actions pipeline configuration

🔐 Deployment Flow
  Developer pushes code to main
  GitHub Actions connects to EC2 via SSH
  Old containers are removed
  Latest code is pulled, Docker image is rebuilt
  New container is deployed and served via port 80
