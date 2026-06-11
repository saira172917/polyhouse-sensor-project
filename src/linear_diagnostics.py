import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------
# Load data + model
# ----------------------------
X_test = pd.read_parquet("data/processed/X_test.parquet")
y_test = pd.read_parquet("data/processed/y_test.parquet").values.ravel()

model = joblib.load("models/linear_regression.joblib")

pred_test = model.predict(X_test)

# ----------------------------
# Residuals
# ----------------------------
residuals = y_test - pred_test

# ----------------------------
# Plots
# ----------------------------
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].scatter(pred_test, residuals, alpha=0.5)
axes[0].axhline(0, color="red", linestyle="--")
axes[0].set(xlabel="Predicted yield (kg)", ylabel="Residual (kg)")

axes[1].scatter(X_test["humidity_pct"], residuals, alpha=0.5)
axes[1].axhline(0, color="red", linestyle="--")
axes[1].set(xlabel="Humidity (%)", ylabel="Residual (kg)")

plt.tight_layout()
plt.savefig("reports/figures/residuals_linear.png", dpi=150)