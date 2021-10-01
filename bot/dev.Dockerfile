FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /bot
COPY requirements.txt /bot/
RUN pip install -r requirements.txt
COPY . /bot/

ENTRYPOINT [ "python3","formica_bot.py"]
