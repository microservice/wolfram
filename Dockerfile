FROM python:alpine

ADD wolfram.py /wolfram.py
RUN pip install requests

ENTRYPOINT  ["python", "wolfram.py"]
