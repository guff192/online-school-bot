# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "gunicorn", "main:init_app" , "--bind", "0.0.0.0:5000", "--worker-class", "aiohttp.GunicornWebWorker" ]

