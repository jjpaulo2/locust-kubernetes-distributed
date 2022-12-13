FROM python:3.10-alpine

COPY ./requirements.txt /srv
COPY ./worker.conf /srv
COPY ./worker.sh /srv

WORKDIR /srv

RUN apk add --update alpine-sdk linux-headers libffi-dev
RUN pip install -r requirements.txt --upgrade

CMD ["sh", "worker.sh"]