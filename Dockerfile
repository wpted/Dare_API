#syntax=docker/dockerfile:1
FROM python:3.11.0b3-bullseye
WORKDIR / app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload"]



