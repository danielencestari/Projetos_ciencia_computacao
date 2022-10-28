from contextlib import suppress
import src.jobs
import src.insights


def get_unique_job_types(path):
    mustRead = src.jobs.read(path)  # chama o metodo de ler o arquivo
    job_types = []  # lista vazia pra começar
    for job in mustRead:
        getAllTypes = job["job_type"]
        if getAllTypes != "":  # pega os typos de job
            job_types.append(getAllTypes)  # adiciona o job_type na lista
    unique_jobs = set(job_types)  # remove os valores repetidos
    return unique_jobs  # retorna a lista de tipos de job


def filter_by_job_type(jobs, job_type):
    return list(filter(lambda job: job["job_type"] == job_type, jobs))


def get_unique_industries(path):
    return set([job["industry"]
                for job in src.jobs.read(path)
                if job["industry"] != ""])


def filter_by_industry(jobs, industry):
    return list(filter(lambda job: job["industry"] == industry, jobs))


def get_max_salary(path):
    salaries = src.jobs.read(path)  # chama o metodo de ler o arquivo
    all_salaries = []  # lista vaziados salarios
    for salary in salaries:
        if salary["max_salary"] != "":  # pega os salarios
            if salary["max_salary"] != "invalid":
                # se o salario nao for invalido dá o appende na lista
                all_salaries.append(int(salary["max_salary"]))

    return max(all_salaries)  # retorna o maior salario


def get_min_salary(path):
    salaries = src.jobs.read(path)  # chama o metodo de ler o arquivo
    all_salaries = []  # lista vaziados salarios
    for salary in salaries:
        if salary["min_salary"] != "":  # pega os salarios
            if salary["min_salary"] != "invalid":
                # se o salario nao for invalido dá o appende na lista
                all_salaries.append(int(salary["min_salary"]))

    return min(all_salaries)  # retorna o maior salario


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
        or job["max_salary"] < job["min_salary"]
    ):
        raise ValueError()
    else:
        return (
            job["min_salary"] <= int(salary)
            and job["max_salary"] >= int(salary)
        )


def filter_by_salary_range(jobs, salary):
    list = []
    for job in jobs:
        with suppress(ValueError):
            if matches_salary_range(job, salary):
                list.append(job)
    return list
