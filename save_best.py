import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv("electricity_bill.csv")
X = pd.get_dummies(df[['units_consumed','num_persons','num_appliances','month']])
y = df['bill_amount']

# Best jo Optuna ne diya
model = RandomForestRegressor(n_estimators=230, max_depth=18, random_state=42)
model.fit(X, y)

# Save
with open('bill_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as bill_model.pkl - Dubai Project 1 Done!")
print(f"Columns: {list(X.columns)}")
