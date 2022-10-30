FROM python:3.10-alpine

COPY ./requirements.txt /srv
COPY ./api /srv/api
COPY ./books_store /srv/books_store
COPY ./gunicorn.conf.py /srv
COPY ./fixture.json /srv
COPY ./manage.py /srv
COPY ./run.sh /srv
COPY ./nginx.conf /etc/nginx/http.d/default.conf

WORKDIR /srv

RUN apk add --update alpine-sdk nginx
RUN pip install -r requirements.txt --upgrade
RUN python3 ./manage.py collectstatic
RUN python3 ./manage.py migrate
RUN python3 ./manage.py loaddata fixture.json

EXPOSE 80

CMD ["sh", "run.sh"]