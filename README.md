# demo_test

## Setup Project using Docker

Just make sure you have installed `docker` in your machine.

## Install Docker

https://docs.docker.com/get-docker/

1. Clone the project from git repository and move into the project directory.

```sh
git clone https://github.com/priteshtagline/demo_test.git
cd demo_test/
```

2. You can just copy the file `.env.template` as `.env` . And please ensure to add your credentials etc.

```sh
cp .env.template .env
```

3. Then run the following command to setup project using docker:

```sh
docker-compose up -d --build
```

4. Migrate the database

```sh
docker-compose exec web python manage.py migrate
```

5. Create a super user with following command; So you can login into the admin site:

```sh
docker-compose exec web python manage.py createsuperuser
```

You can go to the http:///127.0.0.1 to view the application running.

## Docker Development

### Build the docker containers

```sh
docker-compose up -d --build
```

### Stop the containers

```sh
docker-compose stop
```

### Check the docker containers status

```sh
docker-compose ps -a
```

### Check the logs of the docker containers

The below command displays logs of both containers together.

```sh
docker-compose logs -f --tail 20
```

Check the logs for only the database container

```sh
docker-compose logs -f --tail 20 postgres
```

Check the logs for only the django container.

```sh
docker-compose logs -f --tail 20 web
```

### To remove the docker containers

```sh
docker-compose down
```

To remove the docker containers with all the data. `Do not use this command. This will removes all the data of database.`

```sh
docker-compose down -v
```

### Open database at pgadmin4.

Reference `https://towardsdatascience.com/how-to-run-postgresql-and-pgadmin-using-docker-3a6a8ae918b5`

http://127.0.0.1:5050/
Username and password are taken from the `.env.template` file.

Then run the following command to get hostname using docker:

```sh
docker ps --all

# Get postgres database docker postgres id.
docker inspect {docker_postgres_container_id} | grep IPAddress
```

step -> create_server - >  fill up information(hostname(get through above command take a IP Address as a hostname), username, password this take on .env.template) - > save 