FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application
COPY . .

# Run uvicorn (assumes main.py with FastAPI app called "app")
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
