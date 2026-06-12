Polyhouse Sensor Yield Prediction Pipeline

## 📌 Overview
This project is an end-to-end machine learning pipeline that predicts crop yield (`yield_kg`) using environmental sensor data such as temperature, humidity, and CO₂ levels. The pipeline includes data ingestion, cleaning, feature engineering, model training, evaluation, and comparison of multiple models.

---

## 🎯 Objective
To build a predictive system for estimating crop yield in a controlled polyhouse environment and evaluate whether ensemble models (Random Forest) improve performance over a linear baseline.

---

## 📊 Dataset
The dataset contains daily sensor readings:

**Features:**
- temperature_c
- humidity_pct
- co2_ppm

**Target:**
- yield_kg

---

## 🏗️ Project Structure

polyhouse-sensor-project/
│
├── data/
│ ├── raw/
│ ├── interim/
│ └── processed/
│
├── models/
│ ├── yield_model.pkl
│ └── random_forest.joblib
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
│ ├── train_linear_regression.py
│ └── train_random_forest.py
│
└── README.md


---

## 🔄 ML Pipeline Steps

1. **Data Ingestion** – Load raw sensor CSV data  
2. **Data Cleaning** – Handle missing values and inconsistencies  
3. **EDA** – Understand relationships between features and yield  
4. **Feature Engineering** – Create interaction terms (if needed)  
5. **Train-Test Split** – Chronological split (80/20) to avoid data leakage  
6. **Model Training**:
   - Linear Regression (baseline)
   - Random Forest Regressor  
7. **Evaluation** – MAE, RMSE, R²  
8. **Model Saving** – Save trained models for reuse  

---

## 📈 Model Comparison

| Model              | MAE (kg) | RMSE (kg) | R² Score |
|-------------------|----------|-----------|----------|
| Linear Regression | 0.55     | 0.72      | 0.28     |
| Random Forest     | 0.45     | 0.58      | 0.33     |

---

## 📊 Feature Importance (Random Forest)

Top contributing features:
- 🌡️ Temperature → highest influence
- 💧 Humidity → moderate influence
- 🌫️ CO₂ → lower influence

This indicates that yield is more sensitive to temperature and humidity variations.

---

## 🧠 Key Insights

- Random Forest outperforms Linear Regression across all metrics.
- Improvement is moderate due to partially linear relationships in data.
- Dataset size is small, limiting performance gains from complex models.
- Feature importance provides interpretability for decision-making.

---

## 📉 Model Diagnostics (Linear Regression)

Residual analysis shows:
- Some patterns in residuals → model underfitting
- Nonlinear relationships exist in data
- Justifies use of ensemble models

Saved at:

reports/figures/residuals_linear.png


---

## 💾 Model Artifacts

- Linear Model: `models/yield_model.pkl`
- Random Forest: `models/random_forest.joblib`

---

## 🚀 How to Run

### Install dependencies
```bash
pip install -r requirements.txt
Run full pipeline
python src/ingest.py
python src/audit.py
python src/clean.py
python src/eda.py
python src/features.py
python src/train_test_split.py
python src/train_linear_regression.py
python src/train_random_forest.py
🧠 Conclusion

Random Forest provides better predictive performance compared to Linear Regression by capturing nonlinear relationships in environmental data. However, the improvement is moderate, indicating that the dataset has partially linear structure and limited complexity.
