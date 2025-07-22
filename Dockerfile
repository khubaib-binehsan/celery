FROM ubuntu:24.04 AS base

COPY --from=ghcr.io/astral-sh/uv:0.7.2 /uv /uvx /bin/

RUN apt-get update && apt-get clean

ARG AIRFLOW_VERSION="2.10.0"
ARG PYTHON_VERSION="3.12"
ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

WORKDIR /app

RUN uv init --bare --python "${PYTHON_VERSION}"
RUN uv venv --python "${PYTHON_VERSION}"
RUN uv pip install "apache-airflow[celery]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
RUN uv pip install kombu psycopg2-binary

COPY dags/ /app/dags/

ENV AIRFLOW__CORE__DAG_FOLDER="/app/dags"
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False