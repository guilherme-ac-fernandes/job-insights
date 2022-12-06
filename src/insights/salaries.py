from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    # raise NotImplementedError
    jobs = read(path)
    all_max_salary = set()
    for job in jobs:
        if not job["max_salary"] == '' and job["max_salary"].isnumeric():
            all_max_salary.add(int(job["max_salary"]))
    print(max(all_max_salary))
    return max(all_max_salary)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    # raise NotImplementedError
    jobs = read(path)
    all_min_salary = set()
    for job in jobs:
        if not job["min_salary"] == '' and job["min_salary"].isnumeric():
            all_min_salary.add(int(job["min_salary"]))
    print(min(all_min_salary))
    return min(all_min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    # raise NotImplementedError
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError('Job must have valid min_salary and max_salary')

    min_salary, max_salary = str(job["min_salary"]), str(job["max_salary"])

    if not min_salary.isnumeric() or not max_salary.isnumeric():
        raise ValueError('Min_salary and Max_salary must be digit')

    if int(min_salary) > int(max_salary):
        raise ValueError('Max_salary must be greater that min_salary')

    # Aplicação do lstrip para tratamento de salary
    #  negativo proveniente do site FolksTalks
    # source: https://www.folkstalk.com/tech/a-isdigit
    # -for-negatives-with-code-examples/
    if not str(salary).lstrip('-').isnumeric():
        raise ValueError("Salary must be a digit")

    return int(min_salary) <= int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    # raise NotImplementedError
    # return [job for job in jobs if matches_salary_range(job, salary)]
    all_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                all_jobs.append(job)
        except ValueError as error:
            print(error)
    return all_jobs
