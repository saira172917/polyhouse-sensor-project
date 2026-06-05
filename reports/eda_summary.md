# 📊 EDA Summary Report – Polyhouse Sensor Data

## 1. Objective
The objective of this analysis is to understand the relationship between environmental conditions (temperature, humidity, CO₂) and crop yield in a polyhouse environment.

---

## 2. Dataset Overview
- Total records: 365 days
- Time range: 2024-01-01 to 2024-12-30
- Features:
  - Temperature (°C)
  - Humidity (%)
  - CO₂ levels (ppm)
  - Yield (kg)

---

## 3. Key Observations

### 🌡️ Temperature vs Yield
- Temperature remains within a moderate greenhouse range.
- Yield shows slight variation with temperature changes.
- Extremely high or low temperatures are not observed, indicating stable conditions.

---

### 💧 Humidity vs Yield
- Humidity is consistently high (above 75%).
- Moderate positive relationship observed between humidity and yield.
- Very high humidity may reduce yield efficiency slightly.

---

### 🌫️ CO₂ vs Yield
- CO₂ levels fluctuate between 600–1100 ppm.
- Higher CO₂ levels show a mild positive impact on yield.
- Indicates CO₂ enrichment may improve productivity.

---

## 4. Correlation Insights
- CO₂ has a stronger relationship with yield compared to temperature and humidity.
- Temperature and humidity are moderately correlated due to controlled greenhouse conditions.

---

## 5. Key Conclusion
The analysis suggests that CO₂ concentration plays the most important role in influencing crop yield in a controlled polyhouse environment. Maintaining optimal humidity and temperature ensures stable growth, but CO₂ enrichment can further improve yield performance.

---

## 6. Final Note
This analysis is based on simulated sensor data and demonstrates a full data pipeline including ingestion, cleaning, and exploratory data analysis.