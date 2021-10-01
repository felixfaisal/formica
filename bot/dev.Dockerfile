FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /bot
COPY requirements.txt /bot/

