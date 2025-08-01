import os

commands = [
    "cd aws-deploy-app",
    "docker stop $(docker ps -q)",
    "docker rm $(docker ps -a -q)",
    "docker build -t flask-app .",
    "docker run -d -p 80:5000 flask-app"
]

for cmd in commands:
    os.system(cmd)
