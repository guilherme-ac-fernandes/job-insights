from src.pre_built.sorting import sort_by

job_1 = {"min_salary": 100, "date_posted": '2001-12-25', "max_salary": 1000}
job_2 = {"min_salary": 50, "date_posted": '', "max_salary": 2000}
job_3 = {"min_salary": '', "date_posted": '2022-12-25', "max_salary": 3000}
job_4 = {"min_salary": 200, "date_posted": '2011-12-25', "max_salary": ''}

MOCK_JOBS_MAX = [job_1, job_2, job_3, job_4]
MOCK_JOBS_MIN = [job_1, job_2, job_3, job_4]
MOCK_JOBS_DATE = [job_1, job_2, job_3, job_4]

# A função sort_by altera a lista passada como parâmetro,
# resolução proveniente da ajuda na mentoria do instrutor
# Rodrigo Coin Curvo de Ciência da Computação


def test_sort_by_criteria():
    sort_by(MOCK_JOBS_MAX, "max_salary")
    sort_by(MOCK_JOBS_MIN, "min_salary")
    sort_by(MOCK_JOBS_DATE, "date_posted")
    assert MOCK_JOBS_MAX == [job_3, job_2, job_1, job_4]
    assert MOCK_JOBS_MIN == [job_2, job_1, job_4, job_3]
    assert MOCK_JOBS_DATE == [job_3, job_4, job_1, job_2]
