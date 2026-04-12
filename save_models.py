import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from statsmodels.tsa.arima.model import ARIMA
import joblib

# Load and prepare data
path = "data/processed/cleaned_dataset.csv"
data = pd.read_csv(path)
data["created_at"] = pd.to_datetime(data["created_at"])
data = data.sort_values("created_at")

data["fish_kill"] = (
    (data["dissolved_oxygen"] < 3)
    | (data["ammonia"] > 3)
    | (data["ph"] < 5)
    | (data["ph"] > 9)
).astype(int)

# Feature engineering
features = [
    "temperature",
    "turbidity",
    "dissolved_oxygen",
    "ph",
    "ammonia",
    "nitrate",
    "pond",
    "hour",
    "do_lag1",
    "ammonia_lag1",
]

data["hour"] = data["created_at"].dt.hour

data["do_lag1"] = data["dissolved_oxygen"].shift(1)
data["ammonia_lag1"] = data["ammonia"].shift(1)

data = data.dropna()

X = data[features]
y = data["fish_kill"]

split = int(len(data) * 0.8)
X_train = X.iloc[:split]
X_test = X.iloc[split:]
y_train = y.iloc[:split]
y_test = y.iloc[split:]

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
rf.fit(X_train, y_train)
joblib.dump(rf, "models/random_forest.pkl")
print("Saved models/random_forest.pkl")

# Train XGBoost
xgb = XGBClassifier(eval_metric="logloss")
xgb.fit(X_train, y_train)
joblib.dump(xgb, "models/xgboost.pkl")
print("Saved models/xgboost.pkl")

# Train ARIMA on dissolved oxygen
series = data.set_index("created_at")["dissolved_oxygen"]
series = series.resample("1h").mean().dropna()
series = series.asfreq("1h")
model = ARIMA(series, order=(1, 1, 1))
model_fit = model.fit()
joblib.dump(model_fit, "models/arima_model.pkl")
print("Saved models/arima_model.pkl")
