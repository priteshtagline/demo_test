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

# copy the content of the local src directory to the working directory
COPY . /code/

# add entrypoint
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

