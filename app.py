from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI(title="Electricity Bill Predictor - Dubai Ready")

# Model load
with open('bill_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Columns jo model ne seekhe
MODEL_COLS = ['units_consumed', 'num_persons', 'num_appliances', 'month_Apr', 'month_Aug', 'month_Dec', 'month_Feb', 'month_Jan', 'month_Jul', 'month_Jun', 'month_Mar', 'month_May', 'month_Nov', 'month_Oct', 'month_Sep']

@app.get("/")
def home():
    return {"message": "Bill Predictor API Working - Use /predict"}

@app.get("/predict")
def predict(units_consumed: int, num_persons: int, num_appliances: int, month: str = "Jan"):
    # Create input
    data = {
        'units_consumed': [units_consumed],
        'num_persons': [num_persons],
        'num_appliances': [num_appliances],
        'month_Apr': [1 if month=='Apr' else 0],
        'month_Aug': [1 if month=='Aug' else 0],
        'month_Dec': [1 if month=='Dec' else 0],
        'month_Feb': [1 if month=='Feb' else 0],
        'month_Jan': [1 if month=='Jan' else 0],
        'month_Jul': [1 if month=='Jul' else 0],
        'month_Jun': [1 if month=='Jun' else 0],
        'month_Mar': [1 if month=='Mar' else 0],
        'month_May': [1 if month=='May' else 0],
        'month_Nov': [1 if month=='Nov' else 0],
        'month_Oct': [1 if month=='Oct' else 0],
        'month_Sep': [1 if month=='Sep' else 0],
    }
    df = pd.DataFrame(data)[MODEL_COLS]
    bill = model.predict(df)[0]
    return {
        "units": units_consumed,
        "month": month,
        "predicted_bill": int(bill),
        "currency": "INR (Dubai me AED me convert kar dena)"
    }

