import json
import joblib
import pandas as pd
from pathlib import Path

# -----------------------------------
# Model directory
# -----------------------------------
MODEL_DIR = Path("models")

# Global cache
_model = None
_feature_cols = None


# -----------------------------------
# Load model only once
# -----------------------------------
def _load_model():
    global _model, _feature_cols

    if _model is None:

        model_path = MODEL_DIR / "random_forest_tuned.joblib"
        feature_path = MODEL_DIR / "feature_cols.json"

        # Check model exists
        if not model_path.exists():
            raise FileNotFoundError(
                f"Model file not found: {model_path}"
            )

        # Check feature file exists
        if not feature_path.exists():
            raise FileNotFoundError(
                f"Feature file not found: {feature_path}"
            )

        # Load model
        _model = joblib.load(model_path)

        # Load feature names
        _feature_cols = json.loads(
            feature_path.read_text()
        )


# -----------------------------------
# Predict yield
# -----------------------------------
def predict_yield(
    temperature_c=None,
    humidity_pct=None,
    co2_ppm=None,
    sample=None
):

    _load_model()

    # Use sample dictionary if provided
    if sample is not None:
        temperature_c = sample["temperature_c"]
        humidity_pct = sample["humidity_pct"]
        co2_ppm = sample["co2_ppm"]

    # Create DataFrame
    row = pd.DataFrame([{
        "temperature_c": temperature_c,
        "humidity_pct": humidity_pct,
        "co2_ppm": co2_ppm
    }])

    # Ensure correct column order
    row = row[_feature_cols]

    # Predict
    prediction = _model.predict(row)

    return float(prediction[0])


# -----------------------------------
# Test prediction
# -----------------------------------
if __name__ == "__main__":

    try:
        result = predict_yield(
            temperature_c=22.0,
            humidity_pct=88.0,
            co2_ppm=920
        )

        print(f"Predicted Yield (kg): {result:.2f}")

    except FileNotFoundError as e:
        print(f"❌ {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")