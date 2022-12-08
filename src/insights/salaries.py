from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs"""
    return max({int(job["max_salary"])
                for job in read(path)
                if not job["max_salary"] == ""
                and job["max_salary"].isnumeric()})


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs"""
    return min({int(job["min_salary"])
                for job in read(path)
                if not job["min_salary"] == ""
                and job["min_salary"].isnumeric()})


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job"""

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Job must have valid min_salary and max_salary")

    min_salary, max_salary = str(job["min_salary"]), str(job["max_salary"])

    if not min_salary.isnumeric() or not max_salary.isnumeric():
        raise ValueError("Min_salary and Max_salary must be digit")

    if int(min_salary) > int(max_salary):
        raise ValueError("Max_salary must be greater that min_salary")

    # Aplicação do lstrip para tratamento de salary
    # negativo proveniente do site FolksTalks
    # source: https://www.folkstalk.com/tech/a-isdigit
    # -for-negatives-with-code-examples/
    if not str(salary).lstrip("-").isnumeric():
        raise ValueError("Salary must be a digit")
    return int(min_salary) <= int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range"""
    all_jobs = []
    all_errors = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                all_jobs.append(job)
        except ValueError as error:
            all_errors.append(error)
        finally:
            if len(all_errors) > 0:
                print(f"{len(all_errors)} error found")
    return all_jobs
