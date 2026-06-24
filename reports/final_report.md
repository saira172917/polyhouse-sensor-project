🌿 Polyhouse Yield Prediction System

Abstract

This project presents a machine learning-based system for predicting daily crop yield in a controlled polyhouse environment using environmental parameters such as temperature, humidity, and CO₂ concentration. A Random Forest Regressor is trained and optimized to model nonlinear relationships between environmental conditions and yield output. The final system is deployed as an interactive Streamlit application, enabling real-time prediction and decision support for agricultural management.

Index Terms

Agritech, Machine Learning, Random Forest, Yield Prediction, Streamlit, Environmental Monitoring

I. Introduction

Controlled-environment agriculture (CEA) systems such as polyhouses enable optimized crop production through regulation of environmental factors. However, yield prediction remains challenging due to nonlinear and interdependent climatic effects.

This work develops a predictive system that estimates daily crop yield using machine learning techniques, enabling farmers to make data-driven decisions.

II. Problem Statement

Crop yield in polyhouse environments is highly sensitive to microclimatic variations. The objective of this study is to develop a predictive model that:

Estimates daily yield (kg)
Utilizes environmental sensor data
Supports real-time decision-making through a dashboard
III. Dataset Description

The dataset consists of sensor readings collected from a controlled polyhouse environment.

Input Features:
Temperature (°C)
Humidity (%)
CO₂ concentration (ppm)
Target Variable:
Daily crop yield (kg)
IV. Data Preprocessing

The following preprocessing steps were applied:

Handling missing sensor values
Removal of CO₂ spikes and invalid readings
Capping unrealistic humidity values
Ensuring chronological integrity for time-series consistency
V. Exploratory Data Analysis

Key observations include:

Optimal yield occurs at temperatures between 22–26°C
High humidity levels (80–90%) improve stability of yield
Moderate CO₂ concentration enhances growth efficiency

Figures supporting analysis are stored in:

reports/figures/temp_vs_yield.png
reports/figures/humidity_vs_yield.png
reports/figures/co2_vs_yield.png
VI. Feature Engineering and Validation Strategy

A temporal (time-based) train-test split was used instead of random sampling to avoid data leakage.

Rationale:

Random splitting may introduce future information into training, leading to unrealistic performance. Temporal splitting ensures simulation of real-world forecasting conditions.

VII. Model Development

Multiple regression models were evaluated.

Model	Performance	Observation
Linear Regression	Poor	Underfitting
Decision Tree	Moderate	Overfitting
Random Forest	Best	Selected Model
Final Model:

Random Forest Regressor

Hyperparameters:
n_estimators = 100
max_depth = 8
min_samples_leaf = 5
VIII. Results and Evaluation
Performance Metrics (Test Set):
MAE: 0.445 kg
RMSE: 0.562 kg
R² Score: 0.369
Interpretation:

MAE (0.445 kg):
The model’s average prediction error is less than half a kilogram, making it suitable for farm-level estimation tasks.

RMSE (0.562 kg):
Indicates occasional higher deviations but overall stable predictions.

R² (0.369):
Represents moderate explanatory power. This is expected due to:

Limited feature set (only 3 variables)
Absence of biological parameters (substrate quality, spawn rate)
High inherent variability in biological systems

Thus, the model is best suited for trend estimation rather than exact yield prediction.

IX. Actual vs Predicted Analysis

Model predictions closely follow actual yield trends with minor smoothing effects typical of ensemble models.

No major divergence observed
Captures general seasonal variation patterns
Suitable for decision-support applications

Figure:
reports/figures/actual_vs_predicted.png

X. System Architecture
User Input (Streamlit UI)
        ↓
Input Validation
        ↓
Preprocessing Pipeline
        ↓
Trained Random Forest Model
        ↓
Prediction Engine
        ↓
Output Visualization
XI. Deployment

The system is deployed using Streamlit and supports real-time inference.

Features:
Interactive sensor input sliders
Real-time yield prediction
Visualization of yield trends
Lightweight and user-friendly interface
XII. Monitoring Strategy

Basic monitoring mechanisms include:

Logging prediction outputs
Detecting abnormal values
Tracking weekly prediction trends
Future Enhancements:
Data drift detection
Automated retraining pipeline
Alert system for yield drops
XIII. Limitations
Limited dataset size
Only three environmental features used
No pest or disease data included
No external climate integration
XIV. Future Work

Future improvements include:

Integration of additional features (light intensity, soil moisture, ventilation rate)
Use of advanced models (XGBoost, LSTM)
Full cloud deployment with API + database integration
XV. Reproducibility Appendix
Install dependencies:
pip install -r requirements.txt
Train model:
python src/train_gridsearch.py
Run prediction:
python src/predict.py
Launch Streamlit app:
streamlit run app.py
Conclusion

This project demonstrates the application of machine learning techniques for yield prediction in controlled agricultural environments. The Random Forest model provides reliable trend estimation and has been successfully integrated into a real-time Streamlit dashboard for practical deployment.

## 🧠 Reflection

This project helped me understand end-to-end machine learning system development, from data preprocessing to model training and deployment using Streamlit.

One key challenge was handling model consistency across different runs and ensuring reproducibility in predictions. I also learned how environmental factors like temperature, humidity, and CO₂ interact to affect agricultural yield.

Through this project, I gained practical experience in:
- Building ML pipelines
- Model evaluation using MAE, RMSE, and R²
- Deploying ML models as interactive web applications

Future improvements include adding more environmental features and exploring advanced time-series models for better prediction accuracy.