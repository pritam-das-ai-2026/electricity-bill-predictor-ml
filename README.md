# ⚡ Electricity Bill Predictor - Dubai Ready MLOps
BCA Final Year (Pritam Das, Shillong) -> Upgraded to MLOps

**Model:** RandomForest + Optuna (n=230, depth=18)
**Score:** R2 = 0.9963, MAE < 80
**Stack:** Python, Scikit-learn, Optuna, FastAPI, Docker
**API:** /predict?units_consumed=300&num_persons=4&num_appliances=8&month=Jun

Run: uvicorn app:app --reload -> http://127.0.0.1:8000/docs
Docker: docker build -t bill-predictor . && docker run -p 8000:8000 bill-predictor

Author: Pritam Das | Target: AI/ML Engineer Dubai
