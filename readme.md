# Docker Basics Project

This project serves as a beginner's guide to Docker, covering essential commands for building, pushing, pulling, and managing Docker images.


docker file = 

FROM python:3.8-alpine 
COPY . /app
WORKDIR /app
RUN  pip install -r requirements.txt 
CMD python app.py  

- [Docker](https://www.docker.com/) installed on your machine.

## Getting Started

### Building a Docker Image

docker build -t yourusername/yourproject:latest .


docker login
docker push yourusername/yourproject:latest


docker pull yourusername/yourproject:latest



