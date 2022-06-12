# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /online-school-bot

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /online-school-bot/app
EXPOSE 5000
CMD gunicorn main:init_app  --bind 0.0.0.0:$PORT --worker-class aiohttp.GunicornWebWorker

