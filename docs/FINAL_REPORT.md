🌿 Polyhouse Crop Yield Prediction System  
## End-to-End ML Deployment Capstone Project

---

# 1. Problem Statement & Data Description

## Problem
Agricultural yield in polyhouse environments depends on multiple dynamic factors such as temperature, humidity, and CO₂ levels. Manual prediction of yield is unreliable and inconsistent.

This project builds an AI-based system to predict crop yield using environmental sensor inputs.

## Input Features
- Temperature (°C)
- Humidity (%)
- CO₂ (ppm)

## Output
- Predicted crop yield (kg)

---

# 2. Data Cleaning & EDA Highlights

## Data Processing Steps
- Removed missing/null values
- Normalized sensor ranges
- Checked feature correlation
- Detected outliers in extreme climate conditions

## Key Insights
- Temperature has strong impact on yield
- CO₂ improves yield up to optimal range
- Extremely high humidity reduces yield stability

---

# 3. Modeling & Metrics

## Model Used
- Random Forest Regressor

## Why this model?
- Handles non-linear relationships
- Robust to noise
- Performs well on tabular environmental data

## Evaluation Strategy
- Temporal train-test split used (to simulate real-world future prediction)
- Ensures no data leakage from future sensor readings

## Metrics
- MAE (Mean Absolute Error)
- R² Score

---

# 4. Deployment & Monitoring

## Deployment
- Streamlit Cloud used for deployment
- App entry point: `app.py`
- Public URL provided in repository

## Logging System
Each prediction is logged with:
- Timestamp
- Temperature
- Humidity
- CO₂
- Prediction value

Example:

2026-06-20 16:53, 22°C, 75%, 900 ppm → 16.93 kg


## Monitoring Plan
- Track prediction logs daily
- Detect drift if prediction trends shift over time
- Retrain model if:
  - MAE increases > 10%
  - Seasonal shift occurs
  - Sensor calibration changes
  - Every 6 months retraining cycle

---

# 5. Limitations

- Model depends on simulated/static data
- No real IoT sensor integration yet
- CSV logging instead of database storage
- No automated retraining pipeline

---

# 6. Future Improvements

- Integration with real IoT sensors
- Real-time database (MongoDB / Firebase)
- Automated retraining pipeline
- Advanced dashboard (Plotly / Power BI)
- Anomaly detection for sensor failure
- Weather API integration

---

## Iteration Roadmap

### Future Improvements

1. Integrate real IoT sensors for live environmental monitoring.

2. Replace CSV logging with a cloud database.

3. Implement automated model retraining using newly collected data.

4. Add anomaly detection for faulty sensor readings.

5. Create an admin dashboard for viewing prediction logs.

# 7. Conclusion

This project successfully demonstrates a complete machine learning pipeline including:

- Data preprocessing
- Model training
- Real-time prediction system
- Web deployment using Streamlit
- Logging and monitoring system

It provides a scalable foundation for smart agriculture systems using AI.