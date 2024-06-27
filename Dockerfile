FROM python:3.11-slim

RUN apt-get update 
RUN apt-get install -y build-essential 
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /work
COPY . /work
RUN rm -rf /work/eginx

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501
