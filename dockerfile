# Dockerfile
FROM python:3.10

WORKDIR /app

COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
