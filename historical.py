import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import fetch

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def historcal_data(start, end, city):
	lat, lon = fetch.lat_lon(city) # getting variables from another api


	# Make sure all required weather variables are listed here
	# The order of variables in hourly or daily is important to assign them correctly below
	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": lat,
		"longitude": lon,
		"daily": ["temperature_2m_max", "temperature_2m_min", "rain_sum", "precipitation_sum"],
		"timezone": "auto",
		"start_date": start,
		"end_date": end,
	}
	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]
	print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
	print(f"Elevation: {response.Elevation()} m asl")
	print(f"Timezone: {response.Timezone()}{response.TimezoneAbbreviation()}")
	print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

	# Process daily data. The order of variables needs to be the same as requested.
	daily = response.Daily()
	daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
	daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
	daily_rain_sum = daily.Variables(2).ValuesAsNumpy()
	daily_precipitation_sum = daily.Variables(3).ValuesAsNumpy()

	daily_data = {"date": pd.date_range(
		start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
		end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = daily.Interval()),
		inclusive = "left"
	)}

	daily_data["temperature_2m_max"] = daily_temperature_2m_max
	daily_data["temperature_2m_min"] = daily_temperature_2m_min
	daily_data["rain_sum"] = daily_rain_sum
	daily_data["precipitation_sum"] = daily_precipitation_sum

	daily_dataframe = pd.DataFrame(data = daily_data)
	return(daily_dataframe)
""" 	min_temp = daily_temperature_2m_min.tolist()
	max_temp = daily_temperature_2m_max.tolist()
	rain = daily_rain_sum.tolist()
	return(min_temp, max_temp, rain)

daily_dataframe = pd.DataFrame(data = daily_data)
print("\nDaily data\n", daily_dataframe) """