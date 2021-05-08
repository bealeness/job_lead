# Python and Linux Version 
FROM python:3.10.0b1-alpine3.12

COPY requirements.txt /app/requirements.txt

# Configure server
RUN set -ex \
    && pip install --upgrade pip \  
    && pip install --no-cache-dir -r /app/requirements.txt 

# Working directory
WORKDIR /app

ADD . .

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "job_lead.wsgi:application"]

# Heroku
CMD gunicorn job_lead.wsgi:application --bind 0.0.0.0:$PORT
