SHELL := /bin/bash
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
AWS_ACCESS_KEY := $(shell aws --profile default configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY := $(shell aws --profile default configure get aws_secret_access_key)
PROJECT_NAME = content-service-alert

#-----------------------------------------------------------------------
# Rules of Rules : Grouped rules that _doathing_
#-----------------------------------------------------------------------

test: lint pytest

#-----------------------------------------------------------------------
# Testing & Linting
#-----------------------------------------------------------------------

lint:
    export PYTHONPATH=${ROOT_DIR}:$$PYTHONPATH && \
	pylint app && \
	mypy app;

pytest:
	export PYTHONPATH=${ROOT_DIR}:$$PYTHONPATH && \
	py.test -n 4 --cov app tests

#-----------------------------------------------------------------------
# Run Rules
#-----------------------------------------------------------------------
# Run bot in Docker
run-docker:
	docker run -it --name ${PROJECT_NAME} --rm  ${PROJECT_NAME}:latest

#-----------------------------------------------------------------------
# Docker Rules
#-----------------------------------------------------------------------
# Build Docker container
build-dockerimage:
	docker build -t ${PROJECT_NAME} .

build-dockerimage-local:
	docker build -t ${PROJECT_NAME} -f Dockerfile.local . \
	--build-arg accesskey='${AWS_ACCESS_KEY}' \
	--build-arg secretkey='${AWS_SECRET_ACCESS_KEY}'; \

# Deletes stopped containers, unused volumes, and unused networks.
clean-docker:
	docker system prune -a