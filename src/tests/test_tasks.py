import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.celery import add, mul


def test_add():
    result = add.delay(4, 6)
    assert result.get(timeout=10) == 10


def test_mul():
    result = mul.delay(4, 6)
    assert result.get(timeout=10) == 24


# If you want to run the tests eagerly (without a worker), uncomment the following lines.
# and comment out the test functions above.
# import pytest


# @pytest.fixture(autouse=True)
# def celery_eager(monkeypatch):
#     monkeypatch.setenv("CELERY_TASK_ALWAYS_EAGER", "true")
#     yield
#     monkeypatch.delenv("CELERY_TASK_ALWAYS_EAGER")


# def test_add():
#     result = add(4, 6)

#     assert result == 10


# def test_mul():
#     result = mul(4, 6)

#     assert result == 24
