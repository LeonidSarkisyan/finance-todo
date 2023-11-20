FROM python:3.11

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY migrations .
COPY alembic.ini .
COPY docker .
COPY src .

RUN chmod a+x docker/*.sh

RUN alembic upgrade head

CMD gunicorn src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000