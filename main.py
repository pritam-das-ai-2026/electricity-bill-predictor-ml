from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI(title="Dubai Ready - 3 Projects API")


model = pickle.load(open("bill_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Dubai Ready - 3 Projects Running", "projects": ["Bill Predictor", "Job Scam Detector", "CV Shortlist"]}

# Project 1 - Bill
@app.get("/predict")
def predict(units: int, num_persons: int, num_appliances: int, month: int):
    data = pd.DataFrame(
        [[units, num_persons, num_appliances, month]],
        columns=["units_consumed", "num_persons", "num_appliances", "month"]
    )
    prediction = model.predict(data)
    return {"predicted_bill_rs": round(float(prediction[0]), 2)}


@app.get("/scam-check")
def scam_check(job_text: str):
    fake_words = ["whatsapp", "telegram", "fee", "charges", "money", "pay", "easy money", "no interview"]
    text = job_text.lower()
    score = sum(1 for w in fake_words if w in text)
    if score >= 2:
        return {"result": "FAKE JOB - Scam Alert", "score": score, "safety": "Do NOT pay any money"}
    else:
        return {"result": "Looks Real", "score": score, "safety": "Still verify company on LinkedIn"}


@app.get("/resume-score")
def resume_score(skills: str):
    skills = skills.lower()
    must_have = ["python", "sql", "fastapi", "machine learning", "git", "api"]
    found = [s for s in must_have if s in skills]
    score = int((len(found) / len(must_have)) * 100)
    
    if score >= 70:
        status = "SHORTLISTED for Dubai Interview ✅"
    elif score >= 40:
        status = "On Hold - Add more skills"
    else:
        status = "Rejected - Learn more"
    
    return {
        "your_skills": skills,
        "matched": found,
        "score": f"{score}%",
        "status": status,
        "missing": [s for s in must_have if s not in skills]
    }
