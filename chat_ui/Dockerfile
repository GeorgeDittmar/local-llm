# app/Dockerfile

FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y && apt-get install iputils-ping -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
COPY gradio_app.py /app/gradio_app.py

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "gradio_app.py"]