FROM alpine:latest

WORKDIR /app

COPY . .

RUN apk update \
  && apk upgrade \
  && apk add ca-certificates \
  && update-ca-certificates

# Java Installation
RUN apk add --update --no-cache openjdk11 \
  && apk add --update --no-cache openjdk8-jre

# Node.js Installation
RUN apk add --update --no-cache nodejs npm

# Python Installation
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# R Installation
RUN apk add --update --no-cache R

# go Installation
RUN apk add --update --no-cache go

# Mingw Installation
RUN apk add --update --no-cache gcc g++

# ruby Installation
RUN apk add --update --no-cache ruby-rake-compiler

ADD . .

RUN python3 manage.py migrate

CMD [ "python3" , "manage.py", "runserver", "0.0.0.0:8000"]
