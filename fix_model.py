import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("electricity_bill.csv")
print(df.columns.tolist())


month_map = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
df['month'] = df['month'].map(month_map)


X = df[["units_consumed", "num_persons", "num_appliances", "month"]]
y = df["bill_amount"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

pickle.dump(model, open("bill_model.pkl", "wb"))
print("NEW MODEL SAVED - Ab API chalega!")