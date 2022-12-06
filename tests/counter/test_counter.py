import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", 'Python') == 1639


def test_counter_lower_case():
    assert count_ocurrences("data/jobs.csv", 'python') == 1639


def test_counter_upper_case():
    assert count_ocurrences("data/jobs.csv", 'PYTHON') == 1639


def test_counter_different_char_lower_or_upper():
    assert count_ocurrences("data/jobs.csv", 'JavaScriPt') == 122
    assert count_ocurrences("data/jobs.csv", 'JAvAscrIPT') == 122


def test_counter_not_found_words():
    assert count_ocurrences("data/jobs.csv", 'salário') == 0
    assert count_ocurrences("data/jobs.csv", 'título') == 0


def test_counter_fail_file():
    with pytest.raises(FileNotFoundError):
        count_ocurrences("data/jobs.json", 'python')
