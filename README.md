Polyhouse Sensor Yield Prediction System
📌 Overview

This is an end-to-end machine learning system with a Streamlit web application that predicts crop yield (yield_kg) using polyhouse environmental sensor data.

The project covers the full ML lifecycle:

Data ingestion → validation → cleaning → feature engineering → training → evaluation → testing → deployment

It also includes a production-style UI with error handling and automated testing.

🎯 Objective

To predict agricultural yield using environmental conditions and understand their impact on crop productivity.

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
Model evaluation and comparison
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
📁 Project Structure
polyhouse-sensor-project/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .venv/
│
├── src/
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
│   ├── generate.py
│   └── __init__.py
│
├── models/
│   ├── champion.joblib
│   ├── linear_model.joblib
│   ├── random_forest.joblib
│   ├── random_forest_default.joblib
│   ├── random_forest_tuned.joblib
│   ├── best_random_forest.joblib
│   ├── yield_model.pkl
│   ├── feature_cols.json
│   ├── rf_best_params.json
│   ├── minmax_scaler.joblib
│   └── minmax_scaler_train.joblib
│
├── data/
├── reports/
├── tests/
└── docs/
🚀 How to Run
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Run Streamlit app
streamlit run app.py
3️⃣ Run tests
python -m pytest tests/
🔮 Example Prediction
from src.predict import predict_yield

print(predict_yield(
    temperature_c=22,
    humidity_pct=88,
    co2_ppm=920
))
Output:
Predicted Yield (kg): 16.99
The trained model (`model.pkl`) is included in this repository under the `models/` directory and is loaded by `app.py` during prediction.
⚠️ Error Handling
Missing model → friendly error message (no crash)
Invalid inputs → safe exception handling
Streamlit UI remains stable under failure
🚀 Key Improvements

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

In real-world ML systems, clean architecture, testing, and deployment matter more than model complexity.

🌐 Live Demo :

http://localhost:8501/


Live APP URL:
https://polyhouse-sensor-project-jp2gisjeaf84xzw9y9xh2e.streamlit.app/

Presentation link: https://1drv.ms/p/c/d81f6edb00479422/IQDbilYdFIU_TpfSvkpa8vcdASQsnjZ55JYqxT45ktg2xbc?e=OxTSPq