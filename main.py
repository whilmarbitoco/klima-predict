from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
import joblib  

# ---- Load model and scaler at startup ----
model = tf.keras.models.load_model("keras/model.keras", compile=False)
scaler = joblib.load("keras/scaler.save")  # scaler fitted on training data

app = FastAPI()

class WeatherInput(BaseModel):
    data: list 

def mapToJson(data: np.ndarray) -> list:
    """Convert array to JSON-friendly forecast."""
    forecast = []
    for i, row in enumerate(data):
        forecast.append({
            "day": f"Day {i+1}",
            "temperature_c": round(float(row[0]), 2),
            "humidity_percent": round(float(row[1]), 2),
            "rain": max(0, round(float(row[2]), 3)),
            "pressure_hpa": round(float(row[3]), 2),
            "soil_moisture_percent": round(float(row[4]), 2)
        })
    return forecast


@app.get("/")
async def index():
    return "KLIMA Predict by Whilmar Bitoco"


@app.post("/predict")
async def predict(input_data: WeatherInput) -> list:
    x = np.array(input_data.data, dtype=np.float32)

    x_scaled = scaler.transform(x)

    x_input = np.expand_dims(x_scaled, axis=0)

    prediction_scaled = model.predict(x_input)

    prediction_scaled = prediction_scaled.reshape(-1, x.shape[1])  
    prediction_real = scaler.inverse_transform(prediction_scaled)

    return mapToJson(prediction_real)
