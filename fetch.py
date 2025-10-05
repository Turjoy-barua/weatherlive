import requests
import json
from datetime import datetime
from datetime import timezone
import pycountry


api_key = 'c347ad0525998efbcb7008dd10e7d719'


def lat_lon(location):
    user_input = location.lower()
    location_data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_input}&limit={5}&appid={api_key}")
    #print(json.dumps(location_data.json()[0]["country"]))
    lat = location_data.json()[0]["lat"] 
    lon = location_data.json()[0]["lon"]
    country = location_data.json()[0]["country"]
    return (lat, lon, country)

def get_country_name(code):
    try:
        country = pycountry.countries.get(alpha_2=code)
        return country.name if country else code
    except:
        return code  
    
def fetch_from_api(city):#location
    exclude = "minutely, hourly, alerts"
    units = "metric"
    lat, lon, country = lat_lon(city)
    weather_data = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units{units}&exclude={exclude}&appid={api_key}") # todays weather
    formated_current = weather_data.json()["current"]
    
    return formated_current, get_country_name(country) 

        
def fetch_24(year, month, day, city):
    time = int(datetime(year, month, day, tzinfo=timezone.utc).timestamp())
    lat, lon , country = lat_lon(city)
    weather_data = requests.get(f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={api_key}")
    return weather_data.json()











