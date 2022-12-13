FROM python:3.10-alpine

COPY ./requirements.txt /srv
COPY ./locust.conf /srv
COPY ./run.sh /srv

WORKDIR /srv

RUN apk add --update alpine-sdk linux-headers libffi-dev
RUN pip install -r requirements.txt --upgrade

CMD ["sh", "run.sh"]