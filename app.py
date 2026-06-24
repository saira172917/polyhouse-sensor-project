import streamlit as st
import os
import matplotlib.pyplot as plt
import numpy as np

from src.utils.logger import log_prediction
from src.predict import predict_yield

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="Polyhouse Yield System",
    page_icon="🌿",
    layout="centered"
)

# ----------------------------------
# DEBUG (safe after st import)
# ----------------------------------
st.write("RUNNING FILE:", os.path.abspath(__file__))

st.title("🌿 Polyhouse Yield Prediction System")
st.caption("AI-powered agritech monitoring dashboard")

# ----------------------------------
# MODEL METADATA
# ----------------------------------
MODEL_INFO = {
    "model_name": "Random Forest Yield Model",
    "version": "1.0",
    "features": ["Temperature", "Humidity", "CO₂"],
    "output": "Yield (kg)"
}

# ----------------------------------
# SIDEBAR INPUTS
# ----------------------------------
st.sidebar.header("🎛️ Sensor Controls")

temperature = st.sidebar.slider("🌡️ Temperature (°C)", 10.0, 40.0, 22.0, 0.1)
humidity    = st.sidebar.slider("💧 Humidity (%)", 30.0, 100.0, 75.0, 0.5)
co2         = st.sidebar.slider("🫧 CO₂ (ppm)", 300, 2000, 900, 10)

# ----------------------------------
# SMART RISK SCORING
# ----------------------------------
risk_score = 0
alerts = []

if temperature < 15 or temperature > 35:
    risk_score += 35
    alerts.append("🌡️ Temperature out of optimal range (15–35°C)")
elif temperature < 18 or temperature > 32:
    risk_score += 15

if humidity < 50 or humidity > 90:
    risk_score += 35
    alerts.append("💧 Humidity out of optimal range (50–90%)")
elif humidity < 55 or humidity > 85:
    risk_score += 15

if co2 < 400 or co2 > 1500:
    risk_score += 30
    alerts.append("🫧 CO₂ out of optimal range (400–1500 ppm)")
elif co2 < 500 or co2 > 1200:
    risk_score += 10

risk_score = min(risk_score, 100)

# ----------------------------------
# SYSTEM HEALTH STATUS
# ----------------------------------
st.subheader("🚨 System Health Status")

if risk_score < 30:
    st.success(f"🟢 Healthy Conditions — Risk Score: {risk_score}/100")
elif risk_score < 70:
    st.warning(f"🟡 Moderate Risk — Risk Score: {risk_score}/100")
else:
    st.error(f"🔴 High Risk Detected — Risk Score: {risk_score}/100")

col1, col2, col3 = st.columns(3)
col1.metric("🌡️ Temperature", f"{temperature:.1f} °C")
col2.metric("💧 Humidity", f"{humidity:.1f} %")
col3.metric("🫧 CO₂", f"{co2} ppm")

if alerts:
    st.markdown("### ⚠️ Active Alerts")
    for a in alerts:
        st.warning(a)

# ----------------------------------
# PREDICTION BUTTON
# ----------------------------------
if st.button("🔍 Predict Yield", use_container_width=True):
    try:
        with st.spinner("Running model inference..."):
            yield_prediction = predict_yield(
                temperature_c=temperature,
                humidity_pct=humidity,
                co2_ppm=co2
            )

        log_prediction(temperature, humidity, co2, yield_prediction)

        st.success("✅ Prediction completed successfully!")
        st.metric("🌾 Estimated Crop Yield", f"{yield_prediction:.2f} kg")

        st.subheader("📈 Yield vs Temperature")

        temp_range = np.linspace(10, 40, 60)
        yield_curve = [
            predict_yield(temperature_c=t, humidity_pct=humidity, co2_ppm=co2)
            for t in temp_range
        ]

        fig, ax = plt.subplots(figsize=(7, 3.5))
        ax.plot(temp_range, yield_curve, linewidth=2.5)
        ax.axvline(temperature, linestyle="--",
                   linewidth=1.5, label=f"Current: {temperature:.1f}°C")
        ax.set_xlabel("Temperature (°C)")
        ax.set_ylabel("Yield (kg)")
        ax.set_title("Predicted Yield Across Temperature Range")
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        st.pyplot(fig)

    except FileNotFoundError:
        st.error("❌ Model file not found. Train the model first.")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

# ----------------------------------
# MODEL METADATA
# ----------------------------------
with st.expander("📦 Model Metadata"):
    st.json(MODEL_INFO)

# ----------------------------------
# FOOTER
# ----------------------------------
st.divider()
st.caption("Built for agritech ML deployment • Streamlit dashboard ready")