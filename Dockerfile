# Pull Python image
FROM python:3

ENV LIBRARY_PATH=/lib:/usr/lib

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app
