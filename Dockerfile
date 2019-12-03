## Build and install packages
FROM python:3.7-alpine as build-python

RUN apk add --update --no-cache \
    build-base \
    tzdata \
    ca-certificates \
    gettext \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    jpeg-dev \
    libjpeg-turbo-dev \
    libpng-dev \
	libwebp-dev \
	openjpeg-dev \
	tiff-dev \
	zlib-dev \
    postgresql-client \
    postgresql-dev \
    nodejs \
    yarn \
    && rm -rf /var/cache/apk/*

RUN mkdir -p /app
WORKDIR /app

COPY . /app

COPY Pipfile Pipfile.lock /app/
COPY package.json yarn.lock /app/

RUN pip install --no-cache-dir --upgrade -q pip pipenv psycopg2
RUN pipenv install --system --dev
RUN yarn install --non-interactive --no-progress --ignore-optional


## Final images
FROM python:3.7-alpine

MAINTAINER Codecraft Team <team@codecraft63.com>

ENV LANG C.UTF-8

RUN apk add --update --no-cache \
  nodejs \
  yarn \
  postgresql-client \
  ca-certificates \
  tzdata \
  gettext \
  && rm -rf /var/cache/apk/*

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/app/public/}

RUN mkdir -p /app
WORKDIR /app

COPY --from=build-python /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY --from=build-python /app/ /app/

ENV SECRET_KEY=dummy
ENV DATABASE_URL=sqlite:///database.sqlite3
ENV CACHE_URL=dummycache://
ENV REDIS_URL=rediscache://127.0.0.1:6379/1
ENV EMAIL_URL=dummymail://

RUN pwd
RUN STATIC_URL=${STATIC_URL} python manage.py collectstatic --no-input

RUN mkdir -p /app/run/media /app/run/static

EXPOSE 8000
ENV PORT 8000
ENV PYTHONBUFFERED 1
ENV PROCESSES 4

CMD ["uwsgi", "--ini", "/app/settings/wsgi/uwsgi.ini"]

