from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI(title="Bijli Bill Predictor - Dubai Ready")

model = pickle.load(open("bill_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Bill Predictor API is Running"}

@app.get("/predict")
@app.post("/predict")
def predict(units: int, num_persons: int, num_appliances: int, month: int):
    data = pd.DataFrame(
        [[units, num_persons, num_appliances, month]],
        columns=["units_consumed", "num_persons", "num_appliances", "month"]
    )
    prediction = model.predict(data)
    return {"predicted_bill_rs": round(float(prediction[0]), 2)}