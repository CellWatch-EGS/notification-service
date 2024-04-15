FROM python:3.8-alpine

LABEL version="1.0"

WORKDIR /app/

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--port", "8500"]