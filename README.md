🌿 Polyhouse Sensor Yield Prediction Pipeline (Final README)
📌 Overview

This project is an end-to-end machine learning pipeline designed to predict crop yield (yield_kg) using microclimate sensor data collected from a controlled polyhouse environment.

It covers the full ML lifecycle:

data ingestion → validation → cleaning → feature engineering → model training → evaluation → comparison → inference

Two models were evaluated:

📊 Linear Regression (baseline)
🌲 Random Forest Regressor (default + tuned)

The objective is to evaluate whether non-linear ensemble models improve predictive performance over a simple statistical baseline.

🎯 Objective

To build a predictive system for estimating crop yield using environmental variables and analyze relationships between:

🌡 Temperature (°C)
💧 Humidity (%)
🌫 CO₂ levels (ppm)
📊 Dataset
Features:
temperature_c
humidity_pct
co2_ppm
Target:
yield_kg
🏗️ Full Project Directory Structure
polyhouse-sensor-project/
│
├── .venv/                              # Virtual environment
│
├── data/                               # Data storage layers
│   ├── raw/                            # Original dataset
│   │   └── polyhouse_sensors.csv
│   │
│   ├── interim/                        # Intermediate processed data
│   │   ├── 01_loaded.parquet
│   │   └── 02_cleaned.parquet
│   │
│   └── processed/                      # ML-ready datasets
│       ├── features.parquet
│       ├── X_train.parquet
│       ├── X_test.parquet
│       ├── y_train.parquet
│       └── y_test.parquet
│
├── docs/                               # Documentation
│   └── cleaning_log.md
│
├── models/                             # Model artifacts
│   ├── champion.joblib                 # Final selected model
│   ├── linear_model.joblib
│   ├── random_forest_default.joblib
│   ├── random_forest_tuned.joblib
│   ├── best_random_forest.joblib
│   ├── yield_model.pkl
│   ├── feature_cols.json
│   ├── rf_best_params.json
│   ├── minmax_scaler.joblib
│   └── minmax_scaler_train.joblib
│
├── reports/                            # Evaluation reports
│   ├── figures/
│   │   ├── corr_heatmap.png
│   │   ├── pred_vs_actual.png
│   │   ├── residuals_linear.png
│   │   ├── rf_importance.png
│   │   └── scatter_yield.png
│   │
│   ├── model_comparison.csv
│   ├── cv_results.md
│   ├── data_quality.md
│   ├── eda_summary.md
│   ├── linear_diagnostics.md
│   └── limitations.md
│
├── src/                                # Source code
│   ├── ingest.py
│   ├── audit.py
│   ├── clean.py
│   ├── eda.py
│   ├── features.py
│   ├── train_test_split.py
│   ├── linear_model.py
│   ├── linear_diagnostics.py
│   ├── train_random_forest.py
│   ├── train_gridsearch.py
│   ├── train_model_pipeline.py
│   ├── train_full_pipeline.py
│   ├── train_model.py
│   ├── predict.py
│   └── generate.py
│
├── requirements.txt
├── The workflow is.txt
└── README.md
🔄 ML Pipeline Workflow
1. Data Ingestion

Raw CSV → structured dataset

2. Data Validation
Missing values
Schema checks
Outlier detection
3. Data Cleaning
Noise removal
Missing value handling
Type correction
4. EDA
Correlation analysis
Distribution plots
Feature relationships
5. Feature Engineering
Scaling
Feature alignment
6. Train-Test Split

Chronological 80/20 split

7. Model Training
Linear Regression
Random Forest (default + tuned)
8. Hyperparameter Tuning

GridSearchCV optimization

9. Evaluation
MAE
RMSE
R²
10. Inference

Saved model used for prediction

📈 Final Model Comparison
Model	MAE	RMSE	R²
Linear Regression	0.419	0.535	0.427 🏆
Random Forest (Default)	0.449	0.580	0.328
Random Forest (Tuned)	0.445	0.562	0.369
🏆 Champion Model
✔ Selected Model:

Linear Regression

🧠 Why it won:
Lowest MAE → best accuracy
Lowest RMSE → most stable predictions
Highest R² → best variance explanation
Generalizes better than complex models on this dataset

👉 Insight: The dataset has a mostly linear structure, so simpler models perform better than ensembles.

🌲 Feature Importance (RF Insight)
🌡 Temperature → strongest influence
💧 Humidity → moderate influence
🌫 CO₂ → smaller but relevant
📉 Linear Model Diagnostics
Residuals show mild non-linearity
Slight underfitting observed
Justifies testing ensemble models
🚀 How to Run
Install dependencies
pip install -r requirements.txt
Train full pipeline
python src/train_model_pipeline.py
Run inference
python src/predict.py
🔮 Inference Example
from src.predict import predict_yield

print(predict_yield(
    temperature_c=22,
    humidity_pct=88,
    co2_ppm=920
))
Output:
Predicted Yield (kg): 16.99
📊 Outputs Generated
Trained models (.joblib)
Metrics table (CSV)
Correlation heatmaps
Residual plots
Feature importance charts
📌 Conclusion

Linear Regression outperformed Random Forest models, showing that the relationship between environmental conditions and crop yield is largely linear.

Final Insight:

Simple models can outperform complex models when the dataset structure is not highly non-linear.

🟢 PROJECT STATUS: COMPLETE

✔ End-to-end ML pipeline
✔ Model comparison completed
✔ Champion model selected
✔ Inference working
✔ Fully reproducible system
✔ Submission-ready documentation