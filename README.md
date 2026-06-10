# 🌿 Polyhouse Sensor Yield Prediction Pipeline

## 📌 Overview

This project is a **production-style end-to-end machine learning pipeline** designed to analyze polyhouse environmental sensor data and predict crop yield (`yield_kg`).

It demonstrates a full data engineering + ML workflow including:

* Data ingestion and validation
* Data cleaning and auditing
* Exploratory data analysis (EDA)
* Feature engineering
* Time-series aware train-test splitting
* Feature scaling
* Model training and serialization
* Automated pipeline execution

The system is structured to mimic a **real-world ML production workflow**, with separated data layers and modular execution scripts.

---

## 🏗️ Project Architecture

```text id="arch1"
polyhouse-sensor-project/
├── .venv/                         # Python virtual environment
│
├── data/                          # Multi-layer data architecture
│   ├── raw/                       # Original immutable sensor data
│   │   └── polyhouse_sensors.csv
│   │
│   ├── interim/                   # Cleaned & intermediate datasets
│   │   ├── 01_loaded.parquet
│   │   └── 02_cleaned.parquet
│   │
│   └── processed/                 # ML-ready feature datasets
│       └── features.parquet
│
├── docs/                          # Documentation & audit logs
│   └── cleaning_log.md
│
├── models/                        # Trained models & scalers
│   ├── minmax_scaler_train.joblib
│   ├── minmax_scaler.joblib
│   └── yield_model.pkl
│
├── reports/                       # Analysis outputs
│   ├── figures/
│   ├── data_quality.md
│   └── eda_summary.md
│
├── src/                           # Modular pipeline components
│   ├── ingest.py                  # Raw CSV ingestion → parquet
│   ├── audit.py                  # Schema + data validation
│   ├── clean.py                 # Missing values & preprocessing
│   ├── eda.py                   # Statistical analysis & visualization
│   ├── features.py              # Feature engineering pipeline
│   ├── train_test_split.py      # Chronological splitting
│   ├── generate.py              # Master pipeline orchestrator
│
└── README.md
```

---

## 🎯 Project Objective

To build a **robust ML pipeline** that predicts crop yield based on environmental conditions in a polyhouse environment using historical sensor data.

The system aims to:

* Identify relationships between environmental factors and yield
* Ensure clean, validated, and structured data flow
* Generate reproducible ML-ready datasets
* Train a baseline predictive model

---

## 📊 Dataset Description

The dataset consists of polyhouse sensor telemetry:

### Features:

* `temperature_c` → Ambient temperature (°C)
* `humidity_pct` → Relative humidity (%)
* `co2_ppm` → CO₂ concentration (ppm)

### Target:

* `yield_kg` → Crop yield (kg)

---

## 🔄 Pipeline Workflow

### 1. Data Ingestion (`ingest.py`)

* Loads raw CSV sensor data
* Converts to structured Parquet format
* Stores output in `data/interim/01_loaded.parquet`

---

### 2. Data Audit (`audit.py`)

* Validates schema consistency
* Detects missing values and anomalies
* Logs issues in `docs/cleaning_log.md`

---

### 3. Data Cleaning (`clean.py`)

* Handles missing values
* Removes invalid sensor readings
* Produces cleaned dataset:

  * `data/interim/02_cleaned.parquet`

---

### 4. Exploratory Data Analysis (`eda.py`)

* Generates:

  * Correlation heatmaps
  * Scatter plots (Humidity, Temperature, CO₂ vs Yield)
* Produces:

  * `reports/figures/`
  * `reports/eda_summary.md`

---

### 5. Feature Engineering (`features.py`)

Creates advanced features:

* Interaction feature:

```text id="feat1"
temp_humid_interaction = (temperature_c × humidity_pct) / 100
```

* Produces ML-ready dataset:

  * `data/processed/features.parquet`

---

### 6. Train-Test Split (`train_test_split.py`)

* Time-series aware chronological split
* Prevents data leakage

Outputs:

* `X_train`, `X_test`, `y_train`, `y_test`

---

### 7. Model Training (`train_model.py`)

* Model: `RandomForestRegressor`
* Evaluation metrics:

  * MAE
  * R² Score

Model artifacts:

* `models/yield_model.pkl`
* `models/minmax_scaler.joblib`

---

### 8. Pipeline Automation (`generate.py`)

* Executes full workflow sequentially:

  1. Ingestion
  2. Audit
  3. Cleaning
  4. Feature Engineering
  5. Splitting
  6. Training

---

## 📈 Key Insights (EDA)

* CO₂ concentration strongly influences crop yield
* Humidity has a moderate positive relationship with yield
* Temperature impacts yield within an optimal range
* Environmental variables interact to influence productivity

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Matplotlib
* Scikit-learn
* Joblib
* PyArrow (Parquet handling)

---

## 🚀 How to Run

### 1. Install dependencies

```bash id="run1"
pip install -r requirements.txt
```

---

### 2. Run full pipeline

```bash id="run2"
python src/generate.py
```

---

### OR run step-by-step

```bash id="run3"
python src/ingest.py
python src/audit.py
python src/clean.py
python src/eda.py
python src/features.py
python src/train_test_split.py
python src/train_model.py
```

---

## 📦 Outputs Generated

### Data

* Cleaned datasets
* Feature matrices
* Train/test splits

### Reports

* Data quality report
* EDA summary
* Visualizations

### Models

* Trained ML model (`.pkl`)
* Scaler artifacts (`.joblib`)

## 📊 Final Training Results

### Dataset Split
- Train size: 292
- Test size: 73
- Split method: Chronological (80/20)
- Train period: 2024-01-01 → 2024-10-18
- Test period: 2024-10-19 → 2024-12-30

### Feature Scaling
- Method: MinMaxScaler
- Range: [0, 1]
- Fit only on training data

### Model Performance (Baseline)
- MAE: 0.45
- R² Score: 0.32
---

## 🧠 Key Concepts Demonstrated

* Data pipeline architecture (raw → interim → processed)
* Data validation & auditing
* Feature engineering
* Time-series aware splitting
* Leakage prevention
* End-to-end ML workflow design
* Model serialization and reproducibility

---

## 📌 Future Improvements

* Add advanced models (XGBoost / LightGBM)
* Time-series forecasting (LSTM / ARIMA)
* Real-time sensor data streaming
* Dashboard (Streamlit / Power BI)
* Feature importance analysis
* Hyperparameter tuning

---

## 👨‍💻 Author

Polyhouse Sensor Yield Prediction System
End-to-end ML Pipeline Project

---

## ⭐ Status

✔ Fully modular pipeline
✔ Data validation implemented
✔ Feature engineering complete
✔ Baseline ML model trained
✔ Reproducible workflow ready
