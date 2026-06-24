# Monitoring Plan

## Logged Information
- Timestamp
- Temperature
- Humidity
- CO₂
- Predicted Yield

## Example

2026-06-20 10:30
Temp: 24°C
Humidity: 85%
CO₂: 900 ppm
Prediction: 18.72 kg

## Data Drift Scenarios

- Sensor calibration changes
- New sensor firmware affects humidity readings
- Seasonal climate changes
- New crop varieties introduced

## Retrain Triggers
- More than 5% missing predictions
- Average prediction error exceeds 10%
- New season or new crop variety
- Every 6 months