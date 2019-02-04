FROM python:2.7 AS base
WORKDIR /app

FROM base AS dependencies
COPY ./multi_stage_app/requirements.txt ./
RUN pip install -r requirements.txt

FROM dependencies AS build 
WORKDIR /app
COPY  . /app

FROM python:2.7-alpine AS release
WORKDIR /app
COPY --from=dependencies /app/requirements.txt ./
COPY --from=dependencies /root/.cache /root/.cache
RUN pip install -r requirements.txt && rm -rf /root/.cache
COPY --from=build /app ./
CMD ["gunicorn", "--config", "/app/multi_stage_app/conf/gunicorn_config.py", "multi_stage_app.main:app"]
