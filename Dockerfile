FROM python:3.7-slim

COPY . /exerciser-api

WORKDIR /exerciser-api

RUN python3 -m pip install -r requirements.txt

ADD . /exerciser-api

EXPOSE 5006

CMD ["python3", "main.py"]