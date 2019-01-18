SHELL := /bin/bash
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
AWS_ACCESS_KEY := $(shell aws --profile default configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY := $(shell aws --profile default configure get aws_secret_access_key)
PROJECT_NAME = slackbot_boilerplate

#-----------------------------------------------------------------------
# Rules of Rules : Grouped rules that _doathing_
#-----------------------------------------------------------------------
# Auths to AWS ECR and builds image.

build: auth-ecr build-dockerimage

#-----------------------------------------------------------------------
# Run Rules
#-----------------------------------------------------------------------
# Run bot in Docker for local testing
run-docker-local:
	docker run -it --name ${PROJECT_NAME} --rm  ${PROJECT_NAME}:latest

run-docker-remote:
	docker run -it -d --name ${PROJECT_NAME} --rm  ${PROJECT_NAME}:latest

#-----------------------------------------------------------------------
# Docker Rules
#-----------------------------------------------------------------------
# Authenticate to Amazon AWS
auth-ecr:
	`aws ecr get-login --no-include-email`

# Build Docker container
build-dockerimage:
	docker build -t ${PROJECT_NAME} .

# Deletes stopped containers, unused volumes, and unused networks.
clean-docker:
	docker system prune -a