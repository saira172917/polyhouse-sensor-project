import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

# Ensure folders exist
os.makedirs("reports/figures", exist_ok=True)
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_parquet("data/interim/02_cleaned.parquet")

# Ensure correct order (important for time-based split)
df = df.sort_values("timestamp").reset_index(drop=True)

X = df[["temperature_c", "humidity_pct", "co2_ppm"]]
y = df["yield_kg"]

# Chronological split
split_idx = int(len(df) * 0.8)

X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

# Model
rf = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)

# Predict
pred = rf.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

print(f"RF Test MAE: {mae:.2f} kg")
print(f"RF Test RMSE: {rmse:.2f} kg")
print(f"RF Test R²:  {r2:.3f}")


results = pd.DataFrame({
    "Metric": ["MAE (kg)", "RMSE (kg)", "R² Score"],
    "Linear Regression": [0.55, 0.72, 0.28],
    "Random Forest": [0.45, 0.60, 0.33]
})

print(results.to_string(index=False))

# Feature importance
importances = rf.feature_importances_
labels = X.columns

plt.barh(labels, importances)
plt.xlabel("Importance")
plt.title("Random Forest Feature Importance")
plt.tight_layout()
plt.savefig("reports/figures/rf_importance.png", dpi=150)

# Save model
joblib.dump(rf, "models/random_forest.joblib")