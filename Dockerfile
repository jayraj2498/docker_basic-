FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]


# FROM python:3.8-alpine

# # Update Alpine package index and install build-base
# RUN apk update && apk add --no-cache build-base

# # Upgrade pip
# RUN pip install --upgrade pip

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Set the working directory to /app
# WORKDIR /app

# # Install Python dependencies
# RUN pip install -r requirements.txt

# # Command to run the application
# CMD ["python", "app.py"]




# # FROM python:3.8-alpine 
# # COPY . /app
# # WORKDIR /app
# # RUN  pip install -r requirements.txt 
# # CMD python app.py 