## Build and install packages
FROM python:3.7-alpine as build-python

RUN apk add --no-cache /
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
    && rm -rf /var/cache/apk/*

RUN pip install --no-cache-dir --upgrade -q pip pipenv
COPY Pipfile Pipfile.lock /app/
WORKDIR /app
RUN pipenv install --system --deploy --dev


## Final image
FROM python-3.7-alpine

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}

RUN groupadd -r app && useradd -r -g app app

#RUN apk add --no-cache \
#    && rm -rf /var/cache/apk/*

COPY . /app
COPY --from=build-python /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY --from=build-python /app/static /app/static
COPY --from=build-python /app/template /app/templates
WORKDIR /app

RUN SECRET_KEY=dummy STATIC_URL=${STATIC_URL} python3 manage.py collectstatic --no-input

RUN mkdir -p /app/run/media /app/run/static \
    && chown -R app:app /app/

EXPOSE 8000
ENV PORT 8000
ENV PYTHONBUFFERED 1
ENV PROCESSES 4

CMD ["uwsgi", "--ini", "/app/{{ project_name }}/wsgi/uwsgi.ini"]

