FROM python:3.11

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY migrations /fastapi_app
COPY alembic.ini /fastapi_app
COPY docker /fastapi_app
COPY src /fastapi_app

RUN chmod a+x docker/*.sh

RUN alembic upgrade head

CMD gunicorn src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000