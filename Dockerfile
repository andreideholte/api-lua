# docket file for OpenAstroWebService 
# note copies the python deployments (tar.gz) to pip-deployment

FROM python:3.10.5

LABEL Andrei Nascimento "andreideholte@gmail.com"

RUN apt-get update -y && \
    apt-get install gcc

COPY ./requirements.txt /open-astro-web-service/requirements.txt

WORKDIR /open-astro-web-service

RUN pip install -r requirements.txt
RUN pip install kerykeion

COPY ./package.deployment/openastro-1.1.57.tar.gz tmp/
RUN python -m pip install ./tmp/openastro-1.1.57.tar.gz

COPY ./app/*.py /open-astro-web-service/app/
WORKDIR /open-astro-web-service/app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5050"]