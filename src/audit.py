import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/polyhouse_sensor.csv")

print("=== DATASET SHAPE ===")
print(df.shape)

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== NULL COUNTS ===")
print(df.isnull().sum())

print("\n=== SUMMARY STATISTICS ===")
print(df.describe())