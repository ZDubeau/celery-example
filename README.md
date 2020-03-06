# Celery Example

> A simple example of an app using Celery for asynchronous and scheduled tasks

This webapp is built around Flask and Celery to provide a simple email subscription app,
allowing to trigger asynchronous tasks, and schedule tasks at defined time intervals.

The Redis database is used as a message broker to provide transparent asynchronous
event delivery easily with Celery.

## Usage

- `cp .example.env .env`
- `docker-compose up -d`
- `pipenv install -d`
- `pipenv shell`
- `honcho start`
- Open [http://localhost:5000](http://localhost:5000)

## Documentation

- [Celery](https://docs.celeryproject.org)
- [Redis](https://redis.io)
- [Flask](https://flask.palletsprojects.com)
