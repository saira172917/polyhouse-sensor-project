# 🌿 Polyhouse Sensor Yield Prediction Pipeline

## 📌 Overview
This project is an end-to-end machine learning pipeline that predicts crop yield (`yield_kg`) using environmental sensor data from a polyhouse. It includes data ingestion, cleaning, EDA, feature engineering, time-based splitting, model training, evaluation, and diagnostics in a modular workflow.

---

## 🏗️ Project Structure


polyhouse-sensor-project/
│
├── data/
│ ├── raw/
│ ├── interim/
│ └── processed/
│
├── docs/
│
├── models/
│ ├── yield_model.pkl
│ └── minmax_scaler.joblib
│
├── reports/
│ ├── figures/
│ ├── data_quality.md
│ ├── eda_summary.md
│ └── linear_diagnostics.md
│
├── src/
│ ├── ingest.py
│ ├── audit.py
│ ├── clean.py
│ ├── eda.py
│ ├── features.py
│ ├── train_test_split.py
│ ├── train_model.py
│ └── generate.py
│
└── README.md


---

## 🎯 Objective
Build a reliable ML pipeline to predict crop yield based on environmental conditions like temperature, humidity, and CO₂ levels.

---

## 📊 Dataset
Features:
- temperature_c  
- humidity_pct  
- co2_ppm  

Target:
- yield_kg  

---

## 🔄 Pipeline Steps

### 1. Data Ingestion
Loads raw CSV and converts it into structured format.

### 2. Data Audit
Checks schema, missing values, and logs issues.

### 3. Data Cleaning
Handles missing values and removes invalid records.

### 4. EDA
Explores relationships between features and yield using plots and statistics.

### 5. Feature Engineering
Creates interaction features like temperature × humidity.

### 6. Train-Test Split
Chronological split to prevent data leakage.

### 7. Model Training
Trains a Random Forest model and saves it.

---

## 📉 Model Diagnostics (Task 5)

Residuals were analyzed to evaluate model performance.

- Residual = actual − predicted  
- Plots:
  - Residuals vs Predicted
  - Residuals vs Humidity  

Saved at:

reports/figures/residuals_linear.png


Key idea: residuals should look random; patterns indicate model issues.

---

## 📊 Performance
- MAE: 0.45  
- R² Score: 0.32  
- Split: 80/20 (chronological)

---

## 🧠 Key Learnings
- End-to-end ML pipeline design  
- Data validation and cleaning  
- Feature engineering  
- Time-series splitting  
- Model diagnostics using residuals  

---

## 🚀 Run Pipeline
```bash
python src/generate.py

OR step-by-step:

python src/ingest.py
python src/audit.py
python src/clean.py
python src/eda.py
python src/features.py
python src/train_test_split.py
python src/train_model.py
