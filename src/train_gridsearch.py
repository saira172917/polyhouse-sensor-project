import os
import time
import json
import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ----------------------------
# 1. LOAD DATA
# ----------------------------
df = pd.read_parquet("data/interim/02_cleaned.parquet")
df = df.sort_values("timestamp").reset_index(drop=True)

X = df[["temperature_c", "humidity_pct", "co2_ppm"]]
y = df["yield_kg"]

# ----------------------------
# 2. TRAIN-TEST SPLIT (TEMPORAL)
# ----------------------------
split_idx = int(len(df) * 0.8)

X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

# ----------------------------
# 3. PARAMETER RATIONALE (IMPORTANT FOR CHECKLIST)
# ----------------------------
"""
n_estimators:
    Number of trees. More trees → lower variance but higher compute cost.

max_depth:
    Controls tree depth. Prevents overfitting on noisy sensor data.

min_samples_leaf:
    Minimum samples per leaf. Smooths predictions and reduces noise sensitivity.
"""

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 8, 16],
    "min_samples_leaf": [1, 3, 5],
}

# ----------------------------
# 4. TIME SERIES CV (NO LEAKAGE)
# ----------------------------
tscv = TimeSeriesSplit(n_splits=3)

rf = RandomForestRegressor(random_state=42, n_jobs=-1)

# ----------------------------
# 5. GRID SEARCH + RUNTIME TRACKING
# ----------------------------
start_time = time.time()

grid = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1,
    refit=True
)

grid.fit(X_train, y_train)

end_time = time.time()

print("\n🏆 BEST PARAMETERS:")
print(grid.best_params_)

print(f"\n📊 Best CV MAE: {-grid.best_score_:.3f}")
print(f"⏱ Runtime: {end_time - start_time:.2f} seconds")

best_model = grid.best_estimator_

# ----------------------------
# 6. TEST EVALUATION (ONLY ONCE)
# ----------------------------
y_pred = best_model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n🧪 FINAL TEST RESULTS")
print(f"MAE: {mae:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R²: {r2:.3f}")

# ----------------------------
# 7. SAVE MODEL + PARAMETERS
# ----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(best_model, "models/best_random_forest.joblib")
joblib.dump(best_model, "models/champion.joblib")

with open("models/rf_best_params.json", "w") as f:
    json.dump(grid.best_params_, f, indent=4)

print("\n✅ GRID SEARCH COMPLETE — ALL FILES SAVED")