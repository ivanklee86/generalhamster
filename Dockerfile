# Base image
# ---------------------------------------------------------------------- #
FROM python:3
LABEL MAINTAINER="Ivan Lee <ivan@aaptiv.com>"

# Copy app files into the docker image
# ---------------------------------------------------------------------- #
RUN mkdir /slackbot
WORKDIR /slackbot
COPY . /slackbot

# Install dependencies
# ---------------------------------------------------------------------- #
RUN pip install pipenv
RUN pipenv install --system --deploy

# Container settings
# ---------------------------------------------------------------------- #

# Start bot.
# ---------------------------------------------------------------------- #
CMD ["python", "run.py"]