import pandas as pd
import matplotlib.pyplot as plt

# CSV ka naam check karna - tumhare folder me electricity_bill.csv hoga
df = pd.read_csv('electricity_bill.csv')  

print("--- Day 1 EDA ---")
print(df.isnull().sum())
print("\n")
print(df.describe())

# Graph
plt.hist(df['bill_amount'])
plt.title('Bill Amount Distribution')
plt.xlabel('Bill')
plt.ylabel('Count')
plt.show()