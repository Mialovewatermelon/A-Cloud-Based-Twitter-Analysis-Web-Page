FROM python:3.7 as prod


WORKDIR /Demo

ADD . /Demo

ENV HTTP_PROXY "http://wwwproxy.unimelb.edu.au:8000/"
ENV HTTPS_PROXY "http://wwwproxy.unimelb.edu.au:8000/"
ENV NO_PROXY "localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.unimelb.edu.au,.cloud.unimelb.edu.au"

RUN pip install -r REQUIREMENTS.TXT
RUN pip install gunicorn==19.9.0
