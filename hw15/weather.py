# py_simple_gui_client.py
import requests
import PySimpleGUI as sg

sg.theme("DarkBlue3")

layout = [
    [sg.Text("Enter city name:"), sg.InputText(key="city"), sg.Button("Get Weather")],
    [sg.Output(size=(60, 10))]
]

window = sg.Window("FastAPI Weather App", layout)

BASE_URL = "http://127.0.0.1:8000/weather/"

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Get Weather":
        city = values["city"]
        url = f"{BASE_URL}{city}"

        try:
            response = requests.get(url)
            weather_data = response.json()
            sg.Print(f"Weather data for {city}:\n{weather_data}")
        except Exception as e:
            sg.Print(f"Error: {e}")

window.close()
