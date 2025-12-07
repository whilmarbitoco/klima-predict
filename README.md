# Weather Forecasting API

This project provides a RESTful API for weather forecasting using a machine learning model built with TensorFlow/Keras. The API predicts weather parameters such as temperature, humidity, rain, pressure, and soil moisture for a sequence of days, based on recent historical data.

## Features

- **FastAPI** backend for high-performance asynchronous API.
- **TensorFlow/Keras** model for multi-feature weather prediction.
- **Joblib**-serialized scaler for input/output normalization.
- **Easy deployment** with Uvicorn.

## Project Structure

    klima-predict/
    ├── main.py              # FastAPI app: loads model/scaler and defines endpoints
    ├── start.py                 # Script to launch
    ├── models/
    │   ├── model.keras          # Trained Keras model
    │   └── scaler.save          # Scaler used for normalization (joblib)
    ├── requirements.txt         # Python dependencies
    ├── .gitignore               # Git ignore rules
    └── README.md                # Project documentation

## Requirements

- Python 3.8+
- See [requirements.txt](requirements.txt) for dependencies:
  - fastapi
  - uvicorn
  - tensorflow==2.19.0
  - numpy
  - joblib

## Setup

1. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

2. **Ensure model and scaler files exist:**

   - `keras/model.keras` (trained Keras model)
   - `keras/scaler.save` (joblib scaler)

3. **Run the API server:**
   ```sh
   python start.py
   ```
   This will launch the FastAPI app using Uvicorn at `http://0.0.0.0:8000`.

## API Usage

### Endpoint

- **POST** `/predict`

### Request Body

Send a JSON object with a [data](http://_vscodecontentref_/6) field containing a 2D array (list of lists), where each inner list represents a day's weather features:

```json
{
  "data": [
    [27.2, 88.0, 0, 1012, 18],
    [27.4, 87.5, 2, 1011, 21],
    ...
  ]
}
```

Features per row: ` [temperature_c, humidity_percent, rain, pressure_hpa, soil_moisture_percent]`

## Response

Returns a list of forecasted weather for each day:

```json
[
    {
        "day": "Day 1",
        "temperature_c": 28.1,
        "humidity_percent": 87.2,
        "rain": 0,
        "pressure_hpa": 1013.5,
        "soil_moisture_percent": 19.5
    },
...
]
```

## 📄 License

This project is licensed under **All Rights Reserved**.
See the [LICENSE](LICENSE) file for details.
