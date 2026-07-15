FROM python:3.11-slim@sha256:669bbd08353610485a94d5d0c976b4b6498c55280fe42c00f7581f85ee9f3121

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log