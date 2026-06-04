This project is a polyhouse sensor data cleaning pipeline designed to simulate a real-world agritech data engineering workflow. The main objective is to load raw sensor data, audit missing values, clean the dataset using appropriate imputation techniques, and generate a final structured dataset suitable for machine learning applications such as crop yield prediction.



The dataset contains environmental sensor readings from a controlled polyhouse environment, including temperature, humidity, soil moisture, light intensity, CO₂ levels, irrigation status, and yield values. These parameters represent typical agricultural monitoring data used to optimize crop growth conditions.



The pipeline is implemented in Python using modular scripts. The generate\_dataset.py script creates a synthetic dataset with realistic sensor distributions and intentional missing values. The ingest.py script loads the raw CSV data, while audit.py performs exploratory checks such as missing value detection and basic statistical analysis. The clean.py script handles missing data using domain-appropriate strategies such as median imputation for stable environmental variables and forward fill for time-dependent soil moisture readings. The cleaned dataset is then saved in Parquet format for efficient storage and processing.



The final output is a clean, analysis-ready dataset with no missing values, making it suitable for machine learning workflows. This project demonstrates key concepts in data preprocessing, data quality assessment, and pipeline structuring in a real-world agritech scenario.

