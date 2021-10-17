FROM python:3.8-alpine

COPY . /usr/src/

WORKDIR /usr/src/app

RUN pip3 install -r /usr/src/requirements.txt

ENV FLASK_APP=hello.py

CMD flask run --host=0.0.0.0

EXPOSE 5000