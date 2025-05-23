FROM python:3.10.5

LABEL Andrei Nascimento "andreideholte@gmail.com"

RUN apt-get update -y && \
    apt-get install gcc

COPY ./requirements.txt /api-lua/requirements.txt

WORKDIR /api-lua

RUN pip install -r requirements.txt

COPY ./app/*.py /api-lua/app/
COPY ./app/uwsgi.ini /api-lua/app/
WORKDIR /api-lua/app

RUN adduser --disabled-password --gecos '' uwsgiuser

RUN mkdir -p /api-lua/app/cache && chown uwsgiuser:uwsgiuser /api-lua/app/cache
RUN chmod 700 /api-lua/app/cache

USER uwsgiuser

CMD ["uwsgi", "--ini", "uwsgi.ini"]