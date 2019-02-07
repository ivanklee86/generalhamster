SHELL := /bin/bash
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
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

# Deletes stopped containers, unused volumes, and unused networks.
clean-docker:
	docker system prune -a