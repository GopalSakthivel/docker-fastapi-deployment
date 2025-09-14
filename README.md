# 🚀 FastAPI ML App with CI/CD (Docker + GitHub Actions)

This project is a simple **FastAPI ML app** wrapped in Docker and tested with GitHub Actions.

---

## 🔹 Run Locally (without Docker)
You can run it directly with Python:

```
# create venv
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# install dependencies
pip install -r requirements.txt

# train model
python train.py

# start API
uvicorn app:app --host 0.0.0.0 --port 8000
Test API:


curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"features":[5.1,3.5,1.4,0.2]}'
  
🔹 Run with Docker (locally)

docker build -t fastapi-ml-app .
docker run -p 8000:8000 fastapi-ml-app
🔹 Run with GitHub Actions (No Docker needed locally 🎉)
This repo includes a GitHub Actions workflow (.github/workflows/docker-deploy.yml) that:

Installs dependencies

Trains ML model

Builds Docker image

Runs the container inside GitHub Actions VM

Tests the /predict endpoint with curl