# Base image
# ---------------------------------------------------------------------- #
FROM python:3.7
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
ENV PYTHONPATH=/slackbot

# Start bot.
# ---------------------------------------------------------------------- #
CMD ["python", "./app/run.py"]