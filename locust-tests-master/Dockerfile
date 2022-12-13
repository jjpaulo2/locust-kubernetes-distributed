FROM python:3.10-alpine

COPY ./requirements.txt /srv
COPY ./locust.conf /srv
COPY ./run.sh /srv
COPY ./tests /srv/tests

WORKDIR /srv

RUN apk add --update alpine-sdk linux-headers libffi-dev
RUN pip install -r requirements.txt --upgrade

EXPOSE 8881

CMD ["sh", "run.sh"]