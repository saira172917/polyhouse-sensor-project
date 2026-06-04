\# Polyhouse Data Cleaning Log



\## Project

Polyhouse Sensor Yield Forecasting



---



\## 📅 Date

2026-06-04



---



\## 📥 Raw Data Info

\- File: `data/raw/polyhouse\_sensors.csv`

\- Rows: 365

\- Columns: temperature\_c, humidity\_pct, co2\_ppm, yield\_kg, timestamp



---



\## 🧹 Cleaning Steps Performed



\### 1. Duplicate Removal

\- Checked for duplicate rows

\- Action: Removed duplicates (if any)



\### 2. Missing Values Check

\- Checked for null values in dataset

\- Action: Dropped rows with missing values (if any)



\### 3. Data Type Validation

\- Ensured:

&nbsp; - timestamp → datetime

&nbsp; - temperature\_c → float

&nbsp; - humidity\_pct → float

&nbsp; - co2\_ppm → int/float

&nbsp; - yield\_kg → float



---



\##  Output File

\- Cleaned dataset saved at:

&nbsp; `data/processed/polyhouse\_cleaned.csv`



---



\##  Final Result

\- Rows after cleaning: 365 (synthetic dataset had no missing values)

\- Data quality: Clean and ready for ML training



---



\##  Notes

\- Dataset is synthetic, so no major anomalies found

\- Cleaning pipeline is prepared for real sensor data in future

