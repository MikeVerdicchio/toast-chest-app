FROM alpine

RUN mkdir /www
WORKDIR /www
COPY requirements.txt /www/

RUN apk update
RUN apk upgrade
RUN apk --no-cache add \
    python3 \
    python3-dev \
    postgresql-client \
    postgresql-dev \
    build-base \
    gettext

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apk del -r python3-dev postgresql

ENV PYTHONUNBUFFERED 1
COPY . /www/