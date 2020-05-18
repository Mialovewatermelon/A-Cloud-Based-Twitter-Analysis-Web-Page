FROM node:8 as builder

WORKDIR /Demo/appfront
ADD ./appfront /Demo/appfront

RUN npm config set sass_binary_site 
RUN npm install

RUN npm run build
RUN npm cache clean --force \
 && rm -r ./node_modules


FROM python:3.7 as prod


WORKDIR /Demo

ADD . /Demo
COPY --from=builder /Demo/appfront /Demo/appfront

RUN pip install -r REQUIREMENTS.TXT
RUN pip install gunicorn==19.9.0
