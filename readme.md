# Docker Basics Project

This project serves as a beginner's guide to Docker, covering essential commands for building, pushing, pulling, and managing Docker images.

# here is example for creating docker images 

docker file = 

FROM python:3.8-alpine    -># it is th base image it is the first layer (so it will try to  pull the particular image from docker repo  )
COPY . /app               -># . it say abt our local repo  from local repo copy all the file in base image called as app (in my docker image we are creating app folder )        
WORKDIR /app                # our working directory should it  /app 
RUN  pip install -r requirements.txt        # hree all dependencies wrt all liabrary it will present here 
CMD python app.py                           #  it will run tha app.py 



2nd line = these app folser is get creted in the conatainer or docker images 
3rd line = we have to set up our working dierctory  
4th line =  # hree all dependencies wrt all liabrary it will present here it will install 

- [Docker](https://www.docker.com/) installed on your machine.

## Getting Started

### Building a Docker Image

docker build -t yourusername/yourproject:latest .


docker login
docker push yourusername/yourproject:latest


docker pull yourusername/yourproject:latest



