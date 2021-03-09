FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install -y gcc curl git software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update

RUN apt-get install -y python3.9 python3.9-venv python3.9-dev

RUN ln -s /usr/bin/python3.9 /usr/bin/python

# @todo #46 Install ruby.

# @todo #89 Install nodejs.

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

RUN ln -s $HOME/.poetry/bin/poetry /usr/local/bin/poetry

RUN mkdir /app/

WORKDIR /app/
