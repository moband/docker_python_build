FROM python:2.7

WORKDIR /app

COPY ./single_stage_app/requirements.txt ./

RUN pip install -r requirements.txt

COPY  ./single_stage_app /app

EXPOSE 8080

CMD ["python","main.py"]
