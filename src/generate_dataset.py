import pandas as pd
import numpy as np

np.random.seed(42)

rows = 100

timestamps = pd.date_range(
    start="2026-06-01 08:00",
    periods=rows,
    freq="h"
)

data = {
    "timestamp": timestamps,
    "temperature_c": np.random.normal(28, 3, rows).round(1),
    "humidity_pct": np.random.normal(72, 5, rows).round(1),
    "soil_moisture_pct": np.random.normal(45, 4, rows).round(1),
    "light_lux": np.random.normal(15000, 2000, rows).round(1),
    "co2_ppm": np.random.normal(450, 30, rows).round(1),
    "irrigation_on": np.random.choice([0, 1], rows),
    "yield_kg": np.random.normal(3.0, 0.4, rows).round(2)
}

df = pd.DataFrame(data)

# ----------------------------
# Inject missing values (important for your assignment)
# ----------------------------
for col in ["temperature_c", "humidity_pct", "soil_moisture_pct", "light_lux", "co2_ppm"]:
    df.loc[np.random.choice(df.index, 5, replace=False), col] = np.nan

# Save to raw folder
df.to_csv("data/raw/polyhouse_sensor.csv", index=False)

print("100-row dataset created successfully!")
print(df.head())
print("\nShape:", df.shape)