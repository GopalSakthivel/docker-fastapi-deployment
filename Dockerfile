# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy FastAPI app code
COPY app ./app

# Copy pre-trained model
COPY model.pkl .

# Expose port
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
