import pandas as pd, numpy as np
np.random.seed(42)
n=800
units = np.random.randint(40, 650, n)
persons = np.random.randint(1, 7, n)
appliances = np.random.randint(2, 16, n)
months = np.random.choice(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], n)
base = np.where(units<100, units*5.5, np.where(units<300, 100*5.5+(units-100)*7.5, 100*5.5+200*7.5+(units-300)*9.5))
bill = base + persons*55 + appliances*30 + np.random.randint(-90,90,n)

df = pd.DataFrame({
    'units_consumed': units,
    'num_persons': persons,
    'num_appliances': appliances,
    'month': months,
    'bill_amount': bill.astype(int)
})
df.to_csv('electricity_bill.csv', index=False)
print("CSV ban gaya 800 rows ka")