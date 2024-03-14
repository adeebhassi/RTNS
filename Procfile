web: gunicorn RTNS.wsgi --log-file -
worker: celery -A RTNS worker --loglevel=info