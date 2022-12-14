from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them"""
    return {industry["industry"]
            for industry in read(path)
            if not industry["industry"] == ""}


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry"""
    return [job for job in jobs if job["industry"] == industry]
