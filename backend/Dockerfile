FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR '/app'
RUN apt-get update && apt-get install -y \
    build-essential \
    python-dev \
    protobuf-compiler \
    libprotobuf-dev \
    libtokyocabinet-dev \
    python-psycopg2 \
    libgeos-c1 \
    libgdal1-dev \
    libspatialindex-dev
COPY requirements.txt ./
RUN pip install -r requirements.txt 
COPY . .

EXPOSE 8000
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver","0.0.0.0:8000"]
