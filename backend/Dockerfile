FROM python:3.8

WORKDIR /app/
COPY ./ ./
COPY ./scripts/start-reload.sh ./

RUN pip install -r requirements.txt

ENV PYTHONPATH=./app/
