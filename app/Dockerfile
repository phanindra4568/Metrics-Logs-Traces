FROM python:3.9-slim

WORKDIR /app
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



EXPOSE 5000

CMD ["python", "app.py"]
