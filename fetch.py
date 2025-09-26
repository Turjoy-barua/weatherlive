import requests
import json
from datetime import datetime
from datetime import timezone


api_key = 'c347ad0525998efbcb7008dd10e7d719'

def kel_to_c(kelvin):
    return (round(kelvin - 273.15, 1))

def fetch_from_api(location):#location
    user_input = location.lower()
    exclude = "minutely, hourly, alerts, daily"
    units = "metric"
    location_data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_input}&limit={5}&appid={api_key}")
    lat = location_data.json()[0]["lat"] 
    lon = location_data.json()[0]["lon"]
    
    weather_data = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units{units}&exclude={exclude}&appid={api_key}") # todays weather
    current_data = weather_data.json()["current"]#c_ -> current
    formated = json.dumps(current_data, indent=2)
    print(location_data.raise_for_status)
    print(location_data.status_code)
    return current_data

        
def fetch_24(year, month, day, city):
    time = int(datetime(year, month, day, tzinfo=timezone.utc).timestamp())
    location_data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={5}&appid={api_key}")
    lat = location_data.json()[0]["lat"] 
    lon = location_data.json()[0]["lon"]
    weather_data = requests.get(f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={api_key}")
    return weather_data.json()













