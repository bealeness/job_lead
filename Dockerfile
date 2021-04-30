FROM python:3

WORKDIR /job_lead

ADD . /job_lead

COPY requiements.txt /job_lead/

RUN pip install -r requirements.txt

COPY . /job_lead/