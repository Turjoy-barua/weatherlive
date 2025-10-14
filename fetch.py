import requests
import json
from datetime import datetime
from datetime import timezone
import pycountry
from timezonefinder import TimezoneFinder as tzf
import pytz

api_key = 'c347ad0525998efbcb7008dd10e7d719'


def lat_lon(location): # ---> to get the latitude and longitude
    user_input = location.lower()
    location_data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_input}&limit={5}&appid={api_key}")
    #print(json.dumps(location_data.json()[0]["country"]))
    lat = location_data.json()[0]["lat"] 
    lon = location_data.json()[0]["lon"]
    country = location_data.json()[0]["country"]
    return (lat, lon, country)


def get_country_name(code): # ---> used for getting the country name from short version
    try:
        country = pycountry.countries.get(alpha_2=code)
        return country.name if country else code
    except:
        return code  
    
def fetch_from_api(city): # ---> to get current data of today
    exclude = "minutely, hourly, alerts"
    units = "metric"
    lat, lon, country = lat_lon(city)
    weather_data = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units{units}&exclude={exclude}&appid={api_key}") # todays weather
    formated_current = weather_data.json()["current"]
    # print(json.dumps(formated_current))
    zone = tzf().timezone_at(lng=lon, lat=lat) # --> used to find time zone so that there is'nt any problem with sunrise/sunset
    tz = pytz.timezone(zone) # --> time zone info
    return formated_current, get_country_name(country), tz
  

  
def fetch_24(year, month, day, city): # ---> to get bulk data 
    time = int(datetime(year, month, day, tzinfo=timezone.utc).timestamp())
    lat, lon , country = lat_lon(city)
    weather_data = requests.get(f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={api_key}")
    return weather_data.json()










