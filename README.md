# 📦 Automated Web Application Deployment on AWS

This project demonstrates how to automate the deployment of a simple Flask-based web application on an AWS EC2 instance using Docker and GitHub Actions. It features a complete CI/CD pipeline that builds and deploys the app automatically upon every push to the main branch.

---

## 🔧 Tech Stack

- **AWS** (EC2, VPC, Security Groups)
- **Docker**
- **Python / Bash Scripting**
- **GitHub Actions**

---

## 🚀 Features

- Flask-based web app containerized with Docker
- Automated deployment to EC2 using GitHub Actions
- Custom Bash & Python scripts for setup and redeployment
- Secure networking using AWS VPC & Security Groups

---

## 📂 Project Structure
aws-deploy-app/
├── app/ # Flask web application
│ └── app.py
├── Dockerfile # Docker setup for the app
├── requirements.txt
├── setup.sh # Bash script for EC2 environment setup
├── deploy.py # Python script for redeployment
├── .github/
│ └── workflows/
│ └── deploy.yml # GitHub Actions pipeline configuration
└── README.md


---

## 🔐 Deployment Flow

1. Developer pushes code to `main` branch
2. GitHub Actions connects to the EC2 instance via SSH
3. Existing Docker containers are stopped and removed
4. Latest code is cloned and Docker image is rebuilt
5. New container is deployed and served on **port 80**

---


