import os

from celery import Celery, schedules

from . import tasks


celery_broker_url = os.environ.get("CELERY_BROKER_URL")
celery_result_backend = os.environ.get("CELERY_RESULT_BACKEND")

celery_app = Celery("celery_example")

celery_app.conf.update(
    broker_url=celery_broker_url,
    result_backend=celery_result_backend,
    enable_utc=True,
    beat_schedule={
        "talking-clock-every-5s": {
            "task": "tasks.talking_clock",
            "kwargs": {},
            "schedule": 5,
        },
        "send-newsletter-minutely": {
            "task": "tasks.send_newsletter",
            "schedule": schedules.crontab(
                minute="*",
                hour="*",
                day_of_week="*",
                day_of_month="*",
                month_of_year="*",
            ),
        },
    }
)

celery_app.task(
    tasks.talking_clock,
    name="tasks.talking_clock",
    ignore_result=False
)

celery_app.task(
    tasks.subscribe_to_newsletter,
    name="tasks.subscribe_to_newsletter",
    ignore_result=True
)

celery_app.task(
    tasks.send_newsletter,
    name="tasks.send_newsletter",
    ignore_result=True
)
