# docket file for OpenAstroWebService 
# note copies the python deployments (tar.gz) to pip-deployment

FROM python:3.10.5

LABEL Andrei Nascimento "andreideholte@gmail.com"

RUN apt-get update -y && \
    apt-get install gcc

COPY ./requirements.txt /api-lua/requirements.txt

WORKDIR /api-lua

RUN pip install -r requirements.txt

COPY ./app/*.py /api-lua/app/
WORKDIR /api-lua/app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5050"]