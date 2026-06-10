import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

df = pd.read_parquet("data/interim/02_cleaned.parquet").sort_values("timestamp")
feature_cols = ["temperature_c", "humidity_pct", "co2_ppm"]
assert df[feature_cols].isna().sum().sum() == 0, "NaNs in features"
assert df["yield_kg"].isna().sum() == 0, "NaNs in target"

split_idx = int(len(df) * 0.8)
train, test = df.iloc[:split_idx], df.iloc[split_idx:]
assert train["timestamp"].max() < test["timestamp"].min(), "Leakage detected!"
print("Train start:", train["timestamp"].min())
print("Train end:", train["timestamp"].max())

print("Test start:", test["timestamp"].min())
print("Test end:", test["timestamp"].max())
print("Train size:", len(train))
print("Test size:", len(test))
scaler = MinMaxScaler()
X_train = scaler.fit_transform(train[feature_cols])
X_test = scaler.transform(test[feature_cols])
y_train = train["yield_kg"].values
y_test = test["yield_kg"].values



X_train_df = pd.DataFrame(X_train, columns=feature_cols)
X_test_df = pd.DataFrame(X_test, columns=feature_cols)

X_train_df.to_parquet("data/processed/X_train.parquet", index=False)
X_test_df.to_parquet("data/processed/X_test.parquet", index=False)

pd.DataFrame({"yield_kg": y_train}).to_parquet("data/processed/y_train.parquet", index=False)
pd.DataFrame({"yield_kg": y_test}).to_parquet("data/processed/y_test.parquet", index=False)

joblib.dump(scaler, "models/minmax_scaler_train.joblib")

print(f"Train: {train['timestamp'].min()} → {train['timestamp'].max()}")
print(f"Test:  {test['timestamp'].min()} → {test['timestamp'].max()}")