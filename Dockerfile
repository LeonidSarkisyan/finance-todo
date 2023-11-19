FROM python:3.11

COPY requirements.txt .

WORKDIR src

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
