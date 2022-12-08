import math
from datetime import date
from typing import List, Dict


def max_salary_key(job: Dict) -> int:
    """Gets max_salary as a sorting key"""
    try:
        return int(job["max_salary"])
    except (KeyError, TypeError, ValueError):
        return -math.inf


def min_salary_key(job: Dict) -> int:
    """Gets min_salary as a sorting key"""
    try:
        return int(job["min_salary"])
    except (KeyError, TypeError, ValueError):
        return math.inf


def date_posted_key(job: Dict) -> date:
    """Gets date_posted as a sorting key"""
    try:
        return date.fromisoformat(job["date_posted"])
    except (KeyError, TypeError, ValueError):
        return date.min


def sort_by(jobs: List[Dict], criteria: str) -> None:
    """Sorts jobs by a given criteria, in-place"""
    criteria_keys = {
        "date_posted": date_posted_key,
        "max_salary": max_salary_key,
        "min_salary": min_salary_key,
    }

    try:
        key = criteria_keys[criteria]
    except KeyError:
        raise ValueError(f"invalid sorting criteria: {criteria}")

    reverse = criteria in ["max_salary", "date_posted"]

    jobs.sort(key=key, reverse=reverse)
