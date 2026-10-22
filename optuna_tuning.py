import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import optuna
from sklearn.metrics import r2_score

df = pd.read_csv("electricity_bill.csv")
X = pd.get_dummies(df[['units_consumed','num_persons','num_appliances','month']])
y = df['bill_amount']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def objective(trial):
    n_estimators = trial.suggest_int('n_estimators', 50, 300)
    max_depth = trial.suggest_int('max_depth', 5, 30)
    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    return r2_score(y_test, pred)

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=20)

print("Best R2:", study.best_value)
print("Best Params:", study.best_params)
