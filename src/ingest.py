import pandas as pd
import os

RAW_PATH = "data/raw/polyhouse_sensor.csv"

def load_data(path):
    """Load CSV safely"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    df = pd.read_csv(path)
    return df


def basic_validation(df):
    """Check dataset structure"""
    expected_cols = [
        "timestamp",
        "temperature_c",
        "humidity_pct",
        "soil_moisture_pct",
        "light_lux",
        "co2_ppm",
        "irrigation_on",
        "yield_kg"
    ]
    
    missing_cols = [col for col in expected_cols if col not in df.columns]
    
    if missing_cols:
        print(" WARNING: Missing columns:", missing_cols)
    else:
        print(" All expected columns present")


def main():
    df = load_data(RAW_PATH)

    print("\n Data Loaded Successfully")
    print("Shape:", df.shape)

    basic_validation(df)

    print("\n Sample Data:")
    print(df.head())


if __name__ == "__main__":
    main()