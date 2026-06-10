import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import os

# ----------------------------
# 1. Load processed data
# ----------------------------
X_train = pd.read_parquet("data/processed/X_train.parquet")
X_test = pd.read_parquet("data/processed/X_test.parquet")

y_train = pd.read_parquet("data/processed/y_train.parquet").values.ravel()
y_test = pd.read_parquet("data/processed/y_test.parquet").values.ravel()

# ----------------------------
# 2. Create model
# ----------------------------
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# ----------------------------
# 3. Train model
# ----------------------------
model.fit(X_train, y_train)

# ----------------------------
# 4. Predictions
# ----------------------------
y_pred = model.predict(X_test)

# ----------------------------
# 5. Evaluation
# ----------------------------
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n===== MODEL PERFORMANCE =====")
print("MAE:", mae)
print("R2 Score:", r2)

# ----------------------------
# 6. Save model
# ----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/yield_model.pkl")

print("\nModel saved successfully!")