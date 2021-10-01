FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /bot

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3","formica_bot.py"]
