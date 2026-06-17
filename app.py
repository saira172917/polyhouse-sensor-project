
import streamlit as st
import matplotlib.pyplot as plt

from src.predict import predict_yield

# ----------------------------------
# Cache model loading
# ----------------------------------
@st.cache_resource
def load_predictor():
    return predict_yield

predict = load_predictor()

# ----------------------------------
# Page configuration
# ----------------------------------
st.set_page_config(
    page_title="Polyhouse Yield Predictor",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 Polyhouse Yield Predictor")
st.caption("Agritech environmental forecasting from sensor data")

# ----------------------------------
# Sidebar Inputs
# ----------------------------------
with st.sidebar:

    st.header("Sensor Readings")

    temp = st.slider(
        "Temperature (°C)",
        min_value=10.0,
        max_value=35.0,
        value=22.0,
        step=0.1
    )

    humid = st.slider(
        "Humidity (%)",
        min_value=50.0,
        max_value=100.0,
        value=88.0,
        step=0.5
    )

    co2 = st.slider(
        "CO₂ (ppm)",
        min_value=400,
        max_value=2000,
        value=900,
        step=10
    )

# ----------------------------------
# Prediction
# ----------------------------------
if st.button("Predict Yield"):

    kg = predict(temp, humid, co2)

    st.metric(
        label="Estimated Crop Yield",
        value=f"{kg:.2f} kg"
    )

    st.success("Prediction completed successfully!")

    # ------------------------------
    # Optional Sensitivity Chart
    # ------------------------------
    st.subheader("Temperature Sensitivity")

    temps = list(range(10, 36))
    preds = [predict(t, humid, co2) for t in temps]

    fig, ax = plt.subplots()

    ax.plot(temps, preds, linewidth=2)

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Predicted Yield (kg)")
    ax.set_title("Yield vs Temperature")

    st.pyplot(fig)
