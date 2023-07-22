FROM python:3.11-alpine

LABEL "creator"="Samoydyuk Roman"

WORKDIR ./usr/lessons

COPY . .

RUN apk update && apk upgrade && apk add bash
RUN pip3 install -r requirements.txt

CMD pytest -s -v test_folder/*

