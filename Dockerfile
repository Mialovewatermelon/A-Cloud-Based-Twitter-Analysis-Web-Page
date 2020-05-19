FROM python:3.7 as prod


WORKDIR /Demo

ADD . /Demo

RUN pip install -r REQUIREMENTS.TXT
RUN pip install gunicorn==19.9.0
