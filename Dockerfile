FROM ubuntu:latest

ARG APP_UID

ARG APP_GID

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install -y gcc curl git make software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update

RUN apt-get install -y python3.9 python3.9-venv python3.9-dev

RUN ln -s /usr/bin/python3.9 /usr/bin/python

RUN apt-get install -y ruby-full

RUN curl -fsSL https://deb.nodesource.com/setup_15.x | bash -

RUN apt-get install -y nodejs

RUN curl -fsSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

RUN ln -s $HOME/.poetry/bin/poetry /usr/local/bin/poetry

RUN gem install bundler

RUN bundle config set --global path $HOME/.cache

RUN npm install -g npm

RUN mkdir /app/

WORKDIR /app/

RUN groupadd --gid ${APP_GID} app

RUN useradd --uid ${APP_UID} --gid app --create-home app

# @todo #208 Change current user. But unfortunately it will
#  require a lot of changes to be made. Compose file point
#  to the wrong cache directory. Poetry installed to the
#  root user home. Bundler cache directory is part of the
#  root user home as well.
