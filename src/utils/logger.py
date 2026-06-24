import pandas as pd
from datetime import datetime
import os

CSV_FILE = "predictionlog.csv"

def log_prediction(temperature, humidity, co2, prediction):

    data = {
        "timestamp": [datetime.now()],
        "temperature": [temperature],
        "humidity": [humidity],
        "co2": [co2],
        "prediction": [prediction]
    }

    df = pd.DataFrame(data)

    # If file exists → append without header
    if os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(CSV_FILE, index=False)