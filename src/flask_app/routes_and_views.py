from flask import Flask, Blueprint, render_template, request, send_file, abort

from src.insights.jobs import (
    read,
    get_unique_job_types,
    filter_by_job_type,
)
from src.insights.industries import (
    get_unique_industries,
    filter_by_industry,
)

from src.insights.salaries import (
    filter_by_salary_range,
    get_min_salary,
    get_max_salary,
)

from src.flask_app.more_insights import (
    slice_jobs,
    get_int_from_args,
    build_jobs_urls,
)

bp = Blueprint("client", __name__, template_folder="templates")


@bp.route("/.images/job.png")
def flask_image():
    return send_file("../../.images/job.png", mimetype="image/png")


@bp.route("/")
def index():
    md = """
<p align="center">
    <img src="/.images/job.png" alt="Logo da Aplicação" width="800"/>
</p>
<h2 align="center">
    Boas-vindas ao Job Insights<br><br>
</h2>
        """
    return render_template("index.jinja2", md=md)


@bp.route("/jobs")
def list_jobs():
    first_job = get_int_from_args("first_job", 0)
    amount = get_int_from_args("amount", 20)
    salary = get_int_from_args("salary", None)
    industry = request.args.get("industry", None)
    job_type = request.args.get("job_type", None)

    jobs = read(path="data/jobs.csv")
    if industry:
        jobs = filter_by_industry(jobs, industry)
    if job_type:
        jobs = filter_by_job_type(jobs, job_type)
    if salary:
        jobs = filter_by_salary_range(jobs, salary)

    jobs = slice_jobs(jobs, first_job, amount)

    build_jobs_urls(jobs)

    ctx = {
        "jobs": jobs,
        "industries": sorted(get_unique_industries("data/jobs.csv")),
        "job_types": sorted(get_unique_job_types("data/jobs.csv")),
        "previous_job_type": job_type,
        "previous_first": first_job,
        "previous_amount": amount,
        "previous_industry": industry,
        "previous_salary": salary,
        "min_salary": get_min_salary("data/jobs.csv"),
        "max_salary": get_max_salary("data/jobs.csv"),
    }

    return render_template("list_jobs.jinja2", ctx=ctx)


# Implementação da rota de /job/<index> baseada na aplicação
# criado no vídeo do canal freeCodeCamp
# source: https://www.youtube.com/watch?v=Z1RJmh_OqeA


@bp.route("/job/<index>")
def job(index):
    int_index = int(index)
    jobs = read(path="data/jobs.csv")
    if 0 <= int_index <= len(jobs):
        job_index = jobs[int_index]
        # Retorno do status code de 200 proveniente da Documentação do Flask
        # source: https://flask.palletsprojects.com/en/1.1.x/quickstart/
        return render_template("job.jinja2", job=job_index), 200
    else:
        # Utilização do abort para tratamento de erro proveniente
        # da publicação no DigitalOcean
        # source: https://www.digitalocean.com/community/
        # tutorials/how-to-handle-errors-in-a-flask-application
        abort(404)


def init_app(app: Flask):
    app.register_blueprint(bp)
