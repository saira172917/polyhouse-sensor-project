Polyhouse Sensor Yield Prediction System
📌 Overview

This project is an end-to-end machine learning system with a Streamlit web application that predicts crop yield (yield_kg) using real-time polyhouse sensor data.

It includes the full ML lifecycle:

Data ingestion → validation → cleaning → feature engineering → model training → evaluation → testing → deployment

The system also includes a production-style UI, error handling, and automated testing (pytest).

🎯 Objective

To predict agricultural yield based on environmental conditions and analyze their influence on crop productivity.

🌡 Input Features:
Temperature (°C)
Humidity (%)
CO₂ (ppm)
🌾 Output:
Predicted Crop Yield (kg)
🚀 Key Features
🧠 Machine Learning
Linear Regression (baseline)
Random Forest (default + tuned)
Feature alignment using feature_cols.json
Model comparison and evaluation
🌐 Streamlit Web App
Real-time yield prediction
⏳ Loading spinner during inference
📊 Yield vs Temperature visualization
⚠️ Smart risk scoring system
🚨 Environmental alerts
📦 Model metadata viewer
❌ Friendly error handling (no crashes)
🧪 Testing
Pytest-based unit tests
Prediction validation checks
Ensures model reliability
📁 Complete Project Structure
polyhouse-sensor-project/
│
├── app.py                              # 🌐 Streamlit web application (UI dashboard)
├── requirements.txt                    # 📦 Python dependencies
├── README.md                           # 📘 Project documentation
├── .gitignore                          # 🚫 Files excluded from Git tracking
│
├── .venv/                              # 🐍 Virtual environment (DO NOT push to GitHub)
│
├── src/                                # 🧠 Core ML pipeline (backend logic)
│   ├── ingest.py                       # Data ingestion module
│   ├── audit.py                       # Data validation checks
│   ├── clean.py                       # Data cleaning pipeline
│   ├── eda.py                         # Exploratory Data Analysis
│   ├── features.py                    # Feature engineering
│   ├── train_test_split.py            # Train-test splitting logic
│   ├── linear_model.py                # Linear regression training
│   ├── linear_diagnostics.py          # Model diagnostics
│   ├── train_random_forest.py         # RF training (default)
│   ├── train_gridsearch.py            # Hyperparameter tuning
│   ├── train_model_pipeline.py        # Full training pipeline
│   ├── train_full_pipeline.py         # End-to-end training script
│   ├── train_model.py                 # Alternate training script
│   ├── predict.py                     # 🔮 Inference + prediction logic
│   ├── generate.py                    # Synthetic data generation (if used)
│   └── __init__.py                    # Python package initializer
│
├── models/                             # 💾 Saved ML models + artifacts
│   ├── champion.joblib                # Final selected model
│   ├── linear_model.joblib
│   ├── linear_regression.joblib
│   ├── random_forest.joblib
│   ├── random_forest_default.joblib
│   ├── random_forest_tuned.joblib     # ⭐ model currently used in app
│   ├── best_random_forest.joblib
│   ├── yield_model.pkl
│   ├── feature_cols.json              # Feature order reference
│   ├── rf_best_params.json            # Best hyperparameters
│   ├── minmax_scaler.joblib
│   ├── minmax_scaler_train.joblib
│
├── data/                               # 📊 Dataset storage layer
│   ├── raw/
│   │   └── polyhouse_sensors.csv      # Original dataset
│   │
│   ├── interim/
│   │   ├── 01_loaded.parquet
│   │   ├── 02_cleaned.parquet
│   │
│   └── processed/
│       ├── features.parquet
│       ├── X_train.parquet
│       ├── X_test.parquet
│       ├── y_train.parquet
│       └── y_test.parquet
│
├── reports/                            # 📈 Analysis & evaluation outputs
│   ├── figures/
│   │   ├── corr_heatmap.png
│   │   ├── pred_vs_actual.png
│   │   ├── residuals_linear.png
│   │   ├── rf_importance.png
│   │   ├── scatter_yield.png
│   │
│   ├── model_comparison.csv           # Metrics table
│   ├── cv_results.md                  # Cross-validation results
│   ├── data_quality.md                # Data validation report
│   ├── eda_summary.md                 # EDA insights
│   ├── linear_diagnostics.md          # Residual analysis
│   ├── limitations.md                 # Model limitations
│
├── tests/                              # 🧪 Unit testing (pytest)
│   └── test_predict.py                # Prediction validation test
│
└── docs/                               # 📚 Documentation folder
    └── cleaning_log.md               # Data cleaning notes

    Example Prediction
from src.predict import predict_yield

print(predict_yield(
    temperature_c=22,
    humidity_pct=88,
    co2_ppm=920
))
Output:
Predicted Yield (kg): 16.99
⚠️ Error Handling
Missing model → friendly error message (no crash)
Invalid input → safe exception handling
Streamlit UI remains stable under failure
🚀 Key Improvements in This Version

✔ Streamlit dashboard integration
✔ UX enhancements (spinner, metrics, icons)
✔ Smart risk scoring system
✔ Interactive visualization
✔ Pytest integration
✔ Production-style error handling
✔ Fully modular ML pipeline

🟢 Project Status

✔ End-to-end ML pipeline completed
✔ Model comparison done
✔ Streamlit deployment ready
✔ Testing implemented
✔ UX polished
✔ GitHub ready
✔ Submission ready

🧠 Final Insight

In real-world ML systems, clean architecture + reliable deployment + testing is more important than model complexity.
