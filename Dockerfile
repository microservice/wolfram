FROM python:alpine

ADD app.py /app.py
RUN pip install requests

ENTRYPOINT  ["python", "app.py"]
