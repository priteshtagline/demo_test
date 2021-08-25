# https://docs.docker.com/samples/django/

# set base image (host OS)
FROM python:3.9
ENV PYTHONUNBUFFERED=1

# set the working directory in the container
WORKDIR /code

 
# copy the dependencies file to the working directory
COPY requirements.txt /code/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# if occur bad marshal data code error else handled it.
RUN find /usr -name '*.pyc' -delete
RUN pip3 install --upgrade --force-reinstall setuptools

# copy the content of the local src directory to the working directory
COPY . /code/
