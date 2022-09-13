from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_list = [job for job in jobs]
    return jobs_list
