FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

ENV PORT 8000
EXPOSE $PORT

CMD ["python", "main.py"]
