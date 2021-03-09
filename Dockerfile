FROM python:3.9

# @todo #46 Base image should be plain ubuntu distribution. Python
#  should be installed manually in it.

# @todo #46 Install ruby.

# @todo #89 Install nodejs.

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

RUN ln -s $HOME/.poetry/bin/poetry /usr/local/bin/poetry

RUN mkdir /app/

WORKDIR /app/
