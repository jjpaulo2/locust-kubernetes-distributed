FROM prom/statsd-exporter:v0.23.0

COPY ./statsd.conf /statsd/statsd.conf

EXPOSE 9125
EXPOSE 9102

CMD ["--statsd.mapping-config=/statsd/statsd.conf"]
