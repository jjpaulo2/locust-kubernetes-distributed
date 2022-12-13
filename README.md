# Locust distributed load test running on Kubernetes 

(Work In Progress)

A complete ecosystem runing in Kubernetes, to show how to use Locust to do distributed load tests.

### Running

You can run the project using docker compose.

```shell
$ docker compose up --build -d
```

Now, go to the endress bellow:

- http://0.0.0.0:8880/ - Django CRUD API
- http://0.0.0.0:8881/ - Locust Master Front-end

To login into **Django admin** interface, use the credencials bellow:

| Info | Value |
|-|-|
| URL | http://0.0.0.0:8880/admin |
| User | admin |
| Password | 123 |
