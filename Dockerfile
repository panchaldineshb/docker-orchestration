# Set python base image
FROM python:3.5.2

# Create app directory
ADD . /todo
WORKDIR /todo

RUN pip install --upgrade pip

EXPOSE 5000

# Install app dependencies
RUN pip install -r requirements.txt
