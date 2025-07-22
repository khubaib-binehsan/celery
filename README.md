# Airflow, Celery, and RabbitMQ Setup

## Requirements:

- Docker
- Docker Compose

## Setup

```bash
docker compose build airflow-image
docker compose up airflow-init # Required for first time setup
docker compose up -d
```