web: gunicorn celery_example.app:app
worker: celery worker --app celery_example.celery:celery_app
beat: celery beat --app celery_example.celery:celery_app
monitor: celery flower --app celery_example.celery:celery_app