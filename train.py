# train.py
import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200)
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")
