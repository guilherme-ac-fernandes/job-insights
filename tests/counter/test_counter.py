import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", 'python') == 1639
    assert count_ocurrences("data/jobs.csv", 'PYTHON') == 1639
    assert count_ocurrences("data/jobs.csv", 'JavaScriPt') == 122
    assert count_ocurrences("data/jobs.csv", 'JAvAscrIPT') == 122
    assert count_ocurrences("data/jobs.csv", 'salário') == 0
    assert count_ocurrences("data/jobs.csv", 'título') == 0


def test_counter_fail_file():
    with pytest.raises(FileNotFoundError):
        count_ocurrences("data/jobs.json", 'python')
