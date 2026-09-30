FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip intall --no-chache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]