FROM grafana/grafana-oss:9.3.1

COPY ./datasource.yaml /etc/grafana/provisioning/datasources/datasource.yaml
COPY ./dashboards.yaml /etc/grafana/provisioning/dashboards/dashboards.yaml
COPY ./dashboards /etc/grafana/dashboards

ENV GF_AUTH_ANONYMOUS_ENABLED="true"
ENV GF_AUTH_ANONYMOUS_ORG_ROLE="Admin"
ENV GF_AUTH_DISABLE_LOGIN_FORM="true"

EXPOSE 3000
