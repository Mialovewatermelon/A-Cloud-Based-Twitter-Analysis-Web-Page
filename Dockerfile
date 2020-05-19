FROM python:3.7 as prod


WORKDIR /Demo

ADD . /Demo

RUN pip3 install -r REQUIREMENTS.TXT
RUN pip3 install gunicorn==19.9.0
