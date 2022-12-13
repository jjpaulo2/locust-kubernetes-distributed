from multiprocessing import cpu_count


wsgi_app = 'books_store.wsgi:application'
bind = '0.0.0.0:8880'
workers = cpu_count() + 2
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 1
statsd_host = 'statsd-exporter:9125'
