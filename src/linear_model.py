import pandas as pd
import numpy as np
import joblib
import json

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# -----------------------------
# 1. Load data
# -----------------------------
X_train = pd.read_parquet("data/processed/X_train.parquet")
X_test = pd.read_parquet("data/processed/X_test.parquet")

y_train = pd.read_parquet("data/processed/y_train.parquet").values.ravel()
y_test = pd.read_parquet("data/processed/y_test.parquet").values.ravel()


# -----------------------------
# 2. Train model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)


# -----------------------------
# 3. Predict
# -----------------------------
pred_test = model.predict(X_test)


# -----------------------------
# 4. Evaluate
# -----------------------------
mae = mean_absolute_error(y_test, pred_test)
rmse = np.sqrt(mean_squared_error(y_test, pred_test))
r2 = r2_score(y_test, pred_test)

print("\n===== LINEAR REGRESSION RESULTS =====")
print(f"Test MAE:  {mae:.2f}")
print(f"Test RMSE: {rmse:.2f}")
print(f"Test R²:   {r2:.3f}")


# -----------------------------
# 5. Coefficients (interpretable)
# -----------------------------
print("\n===== COEFFICIENTS =====")

for name, coef in zip(X_train.columns, model.coef_):
    print(f"{name}: {coef:.3f}")


# -----------------------------
# 6. Save model
# -----------------------------
joblib.dump(model, "models/linear_regression.joblib")


# -----------------------------
# 7. Save metrics (CHECKLIST FIX)
# -----------------------------
metrics = {
    "model": "LinearRegression",
    "mae": float(mae),
    "rmse": float(rmse),
    "r2": float(r2)
}

with open("reports/metrics_linear.json", "w") as f:
    json.dump(metrics, f, indent=4)


print("\nModel + metrics saved successfully!")