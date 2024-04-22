#
FROM python:3.7-slim

RUN apt-get update
RUN apt-get install -y python3-dev

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY app.py /app

EXPOSE 8080

CMD ["python", "app.py"]