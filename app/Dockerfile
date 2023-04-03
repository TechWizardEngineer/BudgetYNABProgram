FROM python:3.8.10-slim

RUN apt-get update

WORKDIR /app

COPY /requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY /data ./data

COPY /utils ./utils

COPY /routes ./routes

COPY /resources ./resources

COPY /root.py /app/root.py

COPY /main.py /app/main.py

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]



