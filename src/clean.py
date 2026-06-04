import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/polyhouse_sensor.csv")

print("=== NULL COUNTS BEFORE CLEANING ===")
print(df.isnull().sum())

# Temperature: median
df["temperature_c"] = df["temperature_c"].fillna(
    df["temperature_c"].median()
)

# Humidity: median
df["humidity_pct"] = df["humidity_pct"].fillna(
    df["humidity_pct"].median()
)

# Soil moisture: forward fill
df["soil_moisture_pct"] = df["soil_moisture_pct"].ffill()

# Light: median
df["light_lux"] = df["light_lux"].fillna(
    df["light_lux"].median()
)

# CO2: median
df["co2_ppm"] = df["co2_ppm"].fillna(
    df["co2_ppm"].median()
)

print("\n=== NULL COUNTS AFTER CLEANING ===")
print(df.isnull().sum())

# Save cleaned dataset
df.to_parquet(
    "data/processed/02_cleaned.parquet",
    index=False
)

print("\nCleaned dataset saved successfully!")