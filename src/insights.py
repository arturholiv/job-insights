from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = set()
    for job in jobs:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_returned = [job for job in jobs if job["job_type"] == job_type]
    return jobs_returned


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    industries_returned = [job for job in jobs if job["industry"] == industry]
    return industries_returned


def get_min_salary(path):
    jobs = read(path)
    salaries = [
        int(job["min_salary"]) for job in jobs if job["min_salary"].isnumeric()
    ]
    lowest_salary = min(salaries)
    return lowest_salary


def get_max_salary(path):
    jobs = read(path)
    salaries = [
        int(job["max_salary"]) for job in jobs if job["max_salary"].isnumeric()
    ]
    highest_salary = max(salaries)
    return highest_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError('"min_salary" and "max_salary" must be in the field')

    if type(job['min_salary']) != int or type(job['max_salary']) != int:
        raise ValueError('"min_salary" and "max_salary" must be integers')

    if job['min_salary'] > job['max_salary']:
        raise ValueError('"min_salary" is greater than "max_salary"')

    if not isinstance(salary, int):
        raise ValueError("min_salary or max_salary are not a valid integer")

    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
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
    return []
