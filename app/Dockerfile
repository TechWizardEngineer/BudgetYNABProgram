FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

WORKDIR /app

COPY /requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip

RUN pip install --no-cache-dir --index-url=https://pypi.org/simple --upgrade -r /app/requirements.txt

COPY /data ./data
COPY /logging/config.yaml ./logging/config.yaml
COPY /utils ./utils
COPY /routes ./routes
COPY /resources ./resources
COPY /root.py /app/root.py
COPY /main.py /app/main.py

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]
