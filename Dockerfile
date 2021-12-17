FROM 933375035704.dkr.ecr.us-east-1.amazonaws.com/python:3.8.0-alpine

RUN pip install fastapi uvicorn jinja2 aiofiles requests prometheus-fastapi-instrumentator

EXPOSE 8000

COPY . /app

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]