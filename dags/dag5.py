from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "dag5_high_priority",
    default_args=default_args,
    description="A simple CeleryExecutor demo DAG",
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
        queue="high_priority",
    )

    t2 = BashOperator(
        task_id="sleep",
        bash_command="sleep 5",
        queue="high_priority",
    )

    t1 >> t2
