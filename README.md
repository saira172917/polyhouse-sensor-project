# 🌱 Polyhouse Sensor Data Engineering Pipeline

This project is a **polyhouse sensor data engineering and analytics pipeline** designed to simulate a real-world agritech workflow. The goal is to generate, process, clean, and analyze environmental sensor data to understand how greenhouse conditions influence crop yield.

---

##  Objective

The main objective of this project is to:

- Generate realistic polyhouse sensor data
- Perform data ingestion and structured storage
- Clean and validate the dataset
- Conduct exploratory data analysis (EDA)
- Generate statistical and visual reports
- Identify relationships between environmental factors and crop yield

---

##  Dataset Description

The dataset simulates sensor readings from a controlled polyhouse environment and includes:

- Temperature (°C)
- Humidity (%)
- Soil Moisture (%)
- Light Intensity (lux)
- CO₂ Levels (ppm)
- Irrigation Status (0/1)
- Crop Yield (kg)

These features represent key environmental conditions used in precision agriculture to optimize crop production.

---

##  Project Pipeline

The project follows a structured data engineering workflow:

### 1. Data Generation
`generate_dataset.py`
- Creates synthetic sensor data
- Introduces realistic variation and missing values
- Simulates agricultural environment behavior

---

### 2. Data Ingestion
`ingest.py`
- Loads raw CSV data
- Converts data into structured format
- Saves intermediate dataset in Parquet format

---

### 3. Data Cleaning
`clean.py`
- Handles missing values using domain-based strategies:
  - Median imputation for stable sensor readings
  - Forward fill for time-dependent variables
- Removes invalid or inconsistent records
- Outputs cleaned dataset in Parquet format

---

### 4. Exploratory Data Analysis (EDA)
`eda.py`
- Computes descriptive statistics
- Generates correlation heatmaps
- Creates scatter plots (Humidity vs Yield, CO₂ vs Yield, Temperature vs Yield)
- Saves all visualizations in `reports/figures/`

---

### 5. Reporting
- `data_quality.md` → statistical summary report
- `eda_summary.md` → insights from data analysis

---

##  Key Insights

- CO₂ levels show a strong relationship with crop yield
- Humidity has a moderate positive correlation with yield
- Temperature remains within a stable greenhouse range, ensuring controlled growth conditions
- Data quality is high after preprocessing with no missing values in the final dataset

---

## Project Structure

```text
polyhouse-sensor-project/
│
├── data/
│   ├── raw/
│   ├── interim/
│
├── src/
│   ├── generate_dataset.py
│   ├── ingest.py
│   ├── clean.py
│   ├── eda.py
│
├── reports/
│   ├── figures/
│   ├── data_quality.md
│   ├── eda_summary.md
│
├── README.md
└── requirements.txt