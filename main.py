import requests
import json
api_key = 'c347ad0525998efbcb7008dd10e7d719'

user_input = "Paris"
exclude = "minutely, hourly, alerts, daily"
units = "metric"
location_data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_input}&limit={5}&appid={api_key}")
lat = location_data.json()[0]["lat"] 
lon = location_data.json()[0]["lon"]

weather_data = requests.get(
    f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}") # todays weather

c_data = weather_data.json()["current"]#c_ -> current
c_temp = weather_data.json()["current"]["temp"]
c_fl = weather_data.json()["current"]["feels_like"]
c_humidity = weather_data.json()["current"]["humidity"]
c_wind_speed = weather_data.json()["current"]
c_fl = weather_data.json()["current"]
c_fl = weather_data.json()["current"]

formated1 = json.dumps(weather_data.json(), indent=3)
formated2 = json.dumps(location_data.json(), indent=2)
print(json.dumps(c_data, indent=2))

