import fetch
import datetime
import database

def kel_to_c(kelvin):
    return (round(kelvin - 273.15, 1))

def weather_emoji(comment):
    comment = comment.lower()  

    if comment in ["clear", "sunny"]:
        return "☀️"
    elif "few clouds" in comment:
        return "🌤️"
    elif "scattered clouds" in comment:
        return "⛅"
    elif "broken clouds" in comment or "overcast" in comment:
        return "🌥️"
    elif "cloud" in comment:
        return "☁️"
    elif "light rain" in comment or "drizzle" in comment:
        return "🌦️"
    elif "rain" in comment:
        return "🌧️"
    elif "thunderstorm" in comment:
        return "⛈️"
    elif "snow" in comment:
        return "🌨️"
    elif "mist" in comment or "haze" in comment or "fog" in comment:
        return "🌫️"
    elif "wind" in comment:
        return "🌬️"
    elif "tornado" in comment:
        return "🌪️"
    elif "hail" in comment:
        return "🧊"
    else:
        return "☀️"
        
def history():
    data =  database.read_data()
    for row in data:
        print(f"date : {row[1]}\tlocation : {row[2]}\ttemp : {row[3]}\tfeels_like : {row[4]}\thumidity : {row[5]}\twind : {row[6]}\train : {row[7]}")
    return 

def current_weather(location):
    weather_data, country, timez = fetch.fetch_from_api(location)
    date = datetime.datetime.fromtimestamp(weather_data.get("dt"), tz=timez).strftime('%Y-%m-%d')
    sunrise = datetime.datetime.fromtimestamp(weather_data.get("sunrise"), tz=timez).strftime('%H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(weather_data.get("sunset"), tz=timez).strftime('%H:%M:%S')
    total_daytime = (datetime.datetime.strptime(sunset, "%H:%M:%S") - datetime.datetime.strptime(sunrise, '%H:%M:%S')).total_seconds()
    temp = kel_to_c(weather_data.get("temp"))
    fl = kel_to_c(weather_data.get("feels_like"))
    pressure = weather_data.get("pressure")
    humidity = weather_data.get("humidity")
    dew_point = kel_to_c(weather_data.get("dew_point"))
    uvi = weather_data.get("uvi")
    clouds = weather_data.get("clouds")
    visibility = weather_data.get('visibility')/1000
    wind_speed = weather_data.get("wind_speed")
    rain_mm = weather_data.get("rain", {}).get("1h", 0) 
    description = weather_data.get("weather", [{}])[0].get("description", "")
    current_time_loc = datetime.datetime.now(tz=timez).strftime("%H:%M")
    
    #database.store_data(date, location.upper(), temp, fl, humidity, wind_speed, rain_mm)
    
    #print(location.upper(), country, date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm, description, total_daytime, current_time_loc)
    return(location.upper(), country, date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm, description, total_daytime, current_time_loc)