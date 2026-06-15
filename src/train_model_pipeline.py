import os
import time
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import TimeSeriesSplit, cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =========================================================
# 1. SETUP
# =========================================================
os.makedirs("models", exist_ok=True)
os.makedirs("reports", exist_ok=True)
os.makedirs("reports/figures", exist_ok=True)

# =========================================================
# 2. LOAD DATA
# =========================================================
df = pd.read_parquet("data/interim/02_cleaned.parquet")
df = df.sort_values("timestamp").reset_index(drop=True)

X = df[["temperature_c", "humidity_pct", "co2_ppm"]]
y = df["yield_kg"]

# =========================================================
# 3. TRAIN-TEST SPLIT (TIME SERIES)
# =========================================================
split_idx = int(len(df) * 0.8)

X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

# =========================================================
# 4. MODELS
# =========================================================
lin = LinearRegression()
rf_default = RandomForestRegressor(random_state=42, n_jobs=-1)

# =========================================================
# 5. CROSS VALIDATION
# =========================================================
tscv = TimeSeriesSplit(n_splits=5)

lin_cv = -cross_val_score(lin, X_train, y_train, cv=tscv,
                          scoring="neg_mean_absolute_error")

rf_cv = -cross_val_score(rf_default, X_train, y_train, cv=tscv,
                         scoring="neg_mean_absolute_error")

print("\n📊 CROSS VALIDATION RESULTS")
print(f"Linear CV MAE: {lin_cv.mean():.3f} ± {lin_cv.std():.3f}")
print(f"RF CV MAE:     {rf_cv.mean():.3f} ± {rf_cv.std():.3f}")

# =========================================================
# 6. GRID SEARCH (TUNED RF)
# =========================================================
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 8, 16],
    "min_samples_leaf": [1, 3, 5]
}

grid = GridSearchCV(
    RandomForestRegressor(random_state=42, n_jobs=-1),
    param_grid=param_grid,
    cv=TimeSeriesSplit(n_splits=3),
    scoring="neg_mean_absolute_error",
    n_jobs=-1,
    refit=True
)

start = time.time()
grid.fit(X_train, y_train)
end = time.time()

rf_tuned = grid.best_estimator_

print("\n🏆 BEST PARAMETERS:", grid.best_params_)
print(f"📊 Best CV MAE: {-grid.best_score_:.3f}")
print(f"⏱ Runtime: {end - start:.2f}s")

joblib.dump(rf_tuned, "models/random_forest_tuned.joblib")

# =========================================================
# 7. TRAIN MODELS
# =========================================================
lin.fit(X_train, y_train)
rf_default.fit(X_train, y_train)
rf_tuned.fit(X_train, y_train)

# =========================================================
# 8. METRICS FUNCTION
# =========================================================
def metrics(y_true, y_pred):
    return {
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_true, y_pred)),
        "R2": r2_score(y_true, y_pred)
    }

lin_pred = lin.predict(X_test)
rf_def_pred = rf_default.predict(X_test)
rf_tuned_pred = rf_tuned.predict(X_test)

lin_m = metrics(y_test, lin_pred)
rf_d = metrics(y_test, rf_def_pred)
rf_t = metrics(y_test, rf_tuned_pred)

# =========================================================
# 9. RESULTS TABLE
# =========================================================
results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest (Default)",
        "Random Forest (Tuned)"
    ],
    "MAE": [lin_m["MAE"], rf_d["MAE"], rf_t["MAE"]],
    "RMSE": [lin_m["RMSE"], rf_d["RMSE"], rf_t["RMSE"]],
    "R2": [lin_m["R2"], rf_d["R2"], rf_t["R2"]]
})

print("\n📊 MODEL COMPARISON")
print(results.to_markdown(index=False))

results.to_csv("reports/model_comparison.csv", index=False)

# =========================================================
# 10. CHAMPION SELECTION (CLEAN + SAFE)
# =========================================================
best_idx = results["MAE"].idxmin()
champion_name = results.loc[best_idx, "Model"]

print("\n🏆 CHAMPION MODEL:", champion_name)

if champion_name == "Linear Regression":
    champion = lin
elif champion_name == "Random Forest (Default)":
    champion = rf_default
else:
    champion = rf_tuned

joblib.dump(champion, "models/champion.joblib")

# =========================================================
# 11. SAVE BASE MODELS
# =========================================================
joblib.dump(lin, "models/linear_model.joblib")
joblib.dump(rf_default, "models/random_forest_default.joblib")

# =========================================================
# 12. PLOT (CHAMPION)
# =========================================================
if champion_name == "Linear Regression":
    champ_pred = lin_pred
elif champion_name == "Random Forest (Default)":
    champ_pred = rf_def_pred
else:
    champ_pred = rf_tuned_pred

plt.figure()
plt.scatter(y_test, champ_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         "r--")

plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title(f"Champion Model: {champion_name}")

plt.savefig("reports/figures/pred_vs_actual.png", dpi=150)
plt.close()

# =========================================================
# 13. LIMITATIONS
# =========================================================
with open("reports/limitations.md", "w") as f:
    f.write("""
# Limitations

- Limited features (temp, humidity, CO2 only)
- No seasonality or growth-stage data
- Assumes stable polyhouse environment
- May not generalize to outdoor farming
- Predictions are advisory only
""")

# =========================================================
# 14. FEATURE COLS
# =========================================================
feature_cols = ["temperature_c", "humidity_pct", "co2_ppm"]

with open("models/feature_cols.json", "w") as f:
    json.dump(feature_cols, f)

print("\n✅ PIPELINE COMPLETE")