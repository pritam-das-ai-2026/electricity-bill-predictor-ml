import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    'units': [100, 200, 300, 400, 500, 600],
    'bill': [300, 600, 900, 1200, 1500, 1800]
}
df = pd.DataFrame(data)
X = df[['units']]
y = df['bill']

model = LinearRegression()
model.fit(X, y)

with open('bill_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model ban gaya! bill_model.pkl ready hai! 🔥")

test_units = 350
predicted_bill = model.predict([[test_units]])
print(f"{test_units} units ka bill hoga: Rs. {predicted_bill[0]:.2f}")