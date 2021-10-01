FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT [ "sh","entrypoint.sh"]
