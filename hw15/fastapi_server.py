import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

API_KEY = "2377a6d257fdfc1cdc2b4c4e4f79a982"


def get_weather_data(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}"
    weather_data = requests.get(base_url).json()
    return weather_data


@app.get("/weather/{city}")
def get_weather(city: str):
    weather_data = get_weather_data(city)
    if "message" in weather_data and weather_data["cod"] == "404":
        raise HTTPException(status_code=404, detail="City not found")

    return JSONResponse(content=weather_data, media_type="application/json", status_code=200)

uvicorn.run(app, host="127.0.0.1", port=8000)
