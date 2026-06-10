# Polyhouse Yield Prediction Project

## Overview
This project predicts crop yield using sensor data (temperature, humidity, CO₂).

## Pipeline Steps
1. Data cleaning (interim folder)
2. Feature engineering (`features.py`)
3. Scaling using MinMaxScaler
4. Train-test split (time-based)
5. Model training (next step)

## Features Used
- temperature_c
- humidity_pct
- co2_ppm
- temp_humid_interaction

## Output Files
- data/processed/X_train.parquet
- data/processed/X_test.parquet
- models/minmax_scaler.joblib

## How to Run
```bash
python src/features.py