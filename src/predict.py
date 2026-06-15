import json
import joblib
import pandas as pd
from pathlib import Path

MODEL_DIR = Path("models")

# Load model
_model = joblib.load(MODEL_DIR / "random_forest_tuned.joblib")

# Load feature order (important for deployment consistency)
_feature_cols = json.loads((MODEL_DIR / "feature_cols.json").read_text())


def predict_yield(temperature_c=None, humidity_pct=None, co2_ppm=None, sample=None):

    if sample:
        temperature_c = sample["temperature_c"]
        humidity_pct = sample["humidity_pct"]
        co2_ppm = sample["co2_ppm"]

    row = pd.DataFrame([{
        "temperature_c": temperature_c,
        "humidity_pct": humidity_pct,
        "co2_ppm": co2_ppm
    }])

    return float(_model.predict(row)[0])

# ----------------------------
# CLI test
# ----------------------------
if __name__ == "__main__":
    result = predict_yield(22.0, 88.0, 920)
    print("Predicted Yield (kg):", result)