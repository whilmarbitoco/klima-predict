from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

# Load model at startup
model = tf.keras.models.load_model("keras/weather_lstm.keras")

app = FastAPI()

# Input schema (adjust shape: 30 timesteps × 5 features)
class WeatherInput(BaseModel):
    data: list  # e.g., [[26.3, 89.0, 0, 1013, 14], ...]

def mapToJson(data: list) -> list:
    forecast = []
    for i, row in enumerate(data):
        forecast.append({
            "day": f"Day {i+1}",
            "temperature_c": round(row[0], 2),
            "humidity_percent": round(row[1], 2),
            "rain": max(0, round(row[2], 3)),  # clamp negatives to 0
            "pressure_hpa": round(row[3], 2),
            "soil_moisture_percent": round(row[4], 2)
        })
    return forecast

@app.post("/predict")
async def predict(input_data: WeatherInput) -> list:
    # Convert to numpy and reshape
    x = np.array(input_data.data, dtype=np.float32)
    x = np.expand_dims(x, axis=0)  # shape: (1, timesteps, features)

    # Run prediction
    prediction = model.predict(x)
    print(prediction.shape)  # e.g., (1, 15, 5)
    prediction = prediction[0]  # remove batch dimension

    return mapToJson(prediction.tolist())
