import pandas as pd
import numpy as np

from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

# ----------------------------
# 1. LOAD DATA
# ----------------------------
df = pd.read_parquet("data/interim/02_cleaned.parquet")

# Ensure time order
df = df.sort_values("timestamp").reset_index(drop=True)

X = df[["temperature_c", "humidity_pct", "co2_ppm"]]
y = df["yield_kg"]

# ----------------------------
# 2. CHRONOLOGICAL SPLIT
# ----------------------------
split_idx = int(len(df) * 0.8)

X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

# ----------------------------
# 3. MODELS
# ----------------------------
rf = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
lin = LinearRegression()

# ----------------------------
# 4. TIME SERIES CROSS VALIDATION (TRAIN ONLY)
# ----------------------------
tscv = TimeSeriesSplit(n_splits=5)

rf_cv_scores = cross_val_score(
    rf,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

lin_cv_scores = cross_val_score(
    lin,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

rf_cv_mae = -rf_cv_scores
lin_cv_mae = -lin_cv_scores

print("\n📊 Cross-Validation Results (Train Only)\n")
print(f"Random Forest CV MAE: {rf_cv_mae.mean():.3f} ± {rf_cv_mae.std():.3f}")
print(f"Linear Regression CV MAE: {lin_cv_mae.mean():.3f} ± {lin_cv_mae.std():.3f}")

# ----------------------------
# 5. TRAIN FINAL MODELS
# ----------------------------
rf.fit(X_train, y_train)
lin.fit(X_train, y_train)

# ----------------------------
# 6. TEST SET EVALUATION
# ----------------------------
rf_pred = rf.predict(X_test)
lin_pred = lin.predict(X_test)

def evaluate(name, y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    print(f"\n{name} Test Results")
    print(f"MAE: {mae:.3f}")
    print(f"RMSE: {rmse:.3f}")
    print(f"R²: {r2:.3f}")

evaluate("Random Forest", y_test, rf_pred)
evaluate("Linear Regression", y_test, lin_pred)

# ----------------------------
# 7. SAVE MODELS
# ----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(rf, "models/random_forest.joblib")
joblib.dump(lin, "models/linear_model.joblib")

# ----------------------------
# 8. SAVE CV RESULTS
# ----------------------------
os.makedirs("reports", exist_ok=True)

with open("reports/cv_results.md", "w") as f:
    f.write("# Cross Validation Results\n\n")
    f.write(f"Random Forest CV MAE: {rf_cv_mae.mean():.3f} ± {rf_cv_mae.std():.3f}\n")
    f.write(f"Linear Regression CV MAE: {lin_cv_mae.mean():.3f} ± {lin_cv_mae.std():.3f}\n\n")

    f.write("## Interpretation\n")
    if rf_cv_mae.mean() < lin_cv_mae.mean():
        f.write("- Random Forest performs better in cross-validation.\n")
    else:
        f.write("- Linear Regression performs better in cross-validation.\n")

    f.write("- TimeSeriesSplit ensures no future leakage.\n")
    f.write("- CV results show model stability across folds.\n")