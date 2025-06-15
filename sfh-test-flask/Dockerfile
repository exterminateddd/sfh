# syntax=docker/dockerfile:1

FROM python:3.12-alpine

WORKDIR /sfh-flask-docker

COPY requirements.txt .

COPY . .
RUN pip3 install -r requirements.txt


CMD flask --app main.py run --host 0.0.0.0
