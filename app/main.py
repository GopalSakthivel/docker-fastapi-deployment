# app/main.py
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# Load model
model = joblib.load("model.pkl")

app = FastAPI()

class IrisInput(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "FastAPI ML App is running 🚀"}

@app.post("/predict")
def predict(data: IrisInput):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}
