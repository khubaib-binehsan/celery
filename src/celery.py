import os

from celery import Celery

broker_url = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
backend_url = os.getenv("CELERY_RESULT_BACKEND", broker_url)

app = Celery("tasks", broker=broker_url, backend=backend_url)


@app.task
def add(x: float, y: float) -> float:
    return x + y


@app.task
def mul(x: float, y: float) -> float:
    return x * y
