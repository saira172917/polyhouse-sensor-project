"""
Feature Engineering:

1. temperature_c → raw sensor temperature
2. humidity_pct → air humidity level
3. co2_ppm → CO2 concentration
4. temp_humid_interaction = temperature_c * humidity_pct / 100
   (captures combined effect of heat + moisture on plant growth)
"""


import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

# ✅ Create folders if they don't exist
os.makedirs("models", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# Load data
df = pd.read_parquet("data/interim/02_cleaned.parquet").sort_values("timestamp")

df["temp_humid_interaction"] = df["temperature_c"] * df["humidity_pct"] / 100

feature_cols = ["temperature_c", "humidity_pct", "co2_ppm", "temp_humid_interaction"]
X = df[feature_cols]
y = df["yield_kg"]
assert X.isna().sum().sum() == 0, "NaNs found in X"
assert y.isna().sum() == 0, "NaNs found in y"
assert len(X) == len(y), "Mismatch between X and y"

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 🔍 CHECK SCALING RANGE
print("Min:", X_scaled.min())
print("Max:", X_scaled.max())
joblib.dump(scaler, "models/minmax_scaler.joblib")

processed = pd.DataFrame(X_scaled, columns=[c + "_scaled" for c in feature_cols])
processed["yield_kg"] = y.values
processed.to_parquet("data/processed/features.parquet", index=False)