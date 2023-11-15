import requests
from pprint import pprint

API_Key = "2377a6d257fdfc1cdc2b4c4e4f79a982"

city = input(" 도시를 입력해주세요: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)

