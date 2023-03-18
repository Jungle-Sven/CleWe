.ONESHELL:
SHELL = bash

docker_run := docker-compose run --rm
docker_backend := $(docker_run) backend
docker_db := $(docker_run) -d db

-include ./Makefile.properties


start:
	docker-compose up -d --build


migrate:
	$(docker_backend) alembic upgrade head

alembic_history:
	$(docker_backend) alembic history

# downgrade migrations (number indicates how much to downgrade)
downgrade:
	$(docker_backend) alembic downgrade -1

# provide migration name in double quotes
makemigrations:
	$(docker_backend) alembic revision --autogenerate -m ""

build: start \
    migrate \
