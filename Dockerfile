FROM python:3.11

WORKDIR /app

COPY ./src /app
COPY ./requirements.txt /app
COPY ./alembic.ini /app
COPY ./migrations /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY entrypoint.sh ./
ENTRYPOINT ["./entrypoint.sh"]



CMD gunicorn src.main:app --workers 4