# FastAPI ML App with Docker + GitHub Actions CI/CD

This repository demonstrates a **production-like ML deployment pipeline** using:

- A **pre-trained model** (`model.pkl`) — no retraining during CI/CD  
- **FastAPI** for serving predictions (`app/main.py`)  
- **Docker** for packaging the app + model  
- **GitHub Actions** for automated **CI/CD**: build, push, and test  
- **Versioned Docker images**: `latest` and Git commit SHA

---

## 🔹 Project Structure

docker-fastapi-deployment/
├─ .github/workflows/docker-deploy.yml # GitHub Actions CI/CD workflow
├─ app/main.py # FastAPI app for /predict endpoint
├─ model.pkl # Pre-trained model
├─ requirements.txt # Python dependencies
├─ Dockerfile # Docker instructions to build image
└─ README.md # Project explanation

---

## 🔹 How It Works

1. **Pre-trained model**
   - Model is trained separately (locally, in Azure ML, AWS SageMaker, or any pipeline)  
   - Training is **not part of CI/CD**  
   - In real-world projects:
     - There is typically a **scheduled or triggered training job**
       - Example triggers: daily, weekly, or when new data arrives  
       - Managed with tools like **Azure ML pipelines**, **SageMaker pipelines**, or **Airflow**
     - The output is a **versioned model file**, stored in cloud storage or model registry

2. **CI/CD Workflow**
   - Triggered automatically on every push to `main`
   - Steps:
     1. Checkout code
     2. Log in to GitHub Container Registry (GHCR)
     3. Build Docker image:
        - Copies `app/` and `model.pkl`  
        - Tags image as `latest` and Git commit SHA
     4. Push Docker image to GHCR
     5. Test Docker container:
        - Starts container
        - Calls `/predict` endpoint
        - Confirms model works before finishing workflow

3. **Docker**
   - Packages **FastAPI app + pre-trained model + dependencies**
   - On container start, `app/main.py` **loads the model** and serves `/predict`
   - Versioning ensures **traceability**: every image matches a specific commit

---

## 🔹 Local Setup & Testing

1. Install dependencies:

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
Build and run Docker locally:


docker build -t fastapi-ml-app .
docker run -p 8000:8000 fastapi-ml-app
Test the /predict endpoint:


curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features":[5.1,3.5,1.4,0.2]}'
Response example: {"prediction":0}

🔹 CI/CD with GitHub Actions
Workflow: .github/workflows/docker-deploy.yml

Automates build → push → test for every commit

Produces versioned Docker images:

ghcr.io/<username>/fastapi-ml-app:latest
ghcr.io/<username>/fastapi-ml-app:<commit-sha>
Test step ensures /predict endpoint works before pushing → reduces errors in production