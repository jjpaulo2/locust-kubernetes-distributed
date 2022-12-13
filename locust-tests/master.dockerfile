FROM python:3.10-alpine

COPY ./requirements.txt /srv
COPY ./master.conf /srv
COPY ./master.sh /srv
COPY ./tests /srv/tests

WORKDIR /srv

RUN apk add --update alpine-sdk linux-headers libffi-dev
RUN pip install -r requirements.txt --upgrade

EXPOSE 8881
EXPOSE 8882

CMD ["sh", "master.sh"]