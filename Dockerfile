FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip intall --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]