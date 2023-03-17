.ONESHELL:
SHELL = bash

docker_run := docker-compose run --rm
docker_backend := $(docker_run) backend
docker_db := $(docker_run) -d db

docker_run_test := docker-compose -f docker-compose.test.yml run --rm
docker_backend_test := $(docker_run_test) backend
docker_db_test := $(docker_run_test) -d db

image_registry := registry.gitlab.com
image_path := omnihr/backend/service
image_tag := latest

-include ./Makefile.properties

legacy_image_url := local:0.0.1
image_url = $(image_registry)/$(image_path):$(image_tag)

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
