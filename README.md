# Celery Demo

## Setup

1. Start Redis:
   ```bash
   docker-compose up -d
   ```
2. Install dependencies:
   ```bash
   uv sync
   ```

## Running a Worker

```bash
uv run celery -A src.celery worker --loglevel=info
```

## Sending a Task

```bash
uv run -m src.scripts.send_task
```

## Running Tests

```bash
uv run pytest
```