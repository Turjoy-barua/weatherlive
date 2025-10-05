import fetch
import datetime
#import time
import os 
import database
import visual

def kel_to_c(kelvin):
    return (round(kelvin - 273.15, 1))

def user_interface():
    print('''========================================
        WEATHER ANALYZER - NSI
========================================
1. Current weather of a city  -> current
2. View saved weather history -> history
3. Analyze weather trends     -> trend 
4. Exit                       -> exit
''') # --> should erase the 3rd option

def history():
    data =  database.read_data()
    for row in data:
        print(f"date : {row[1]}\tlocation : {row[2]}\ttemp : {row[3]}\tfeels_like : {row[4]}\thumidity : {row[5]}\twind : {row[6]}\train : {row[7]}")
    return 

def current_weather(location):
    weather_data, country = fetch.fetch_from_api(location)
    date = datetime.datetime.fromtimestamp(weather_data.get("dt")).strftime('%Y-%m-%d')
    sunrise = datetime.datetime.fromtimestamp(weather_data.get("sunrise")).strftime('%H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(weather_data.get("sunset")).strftime('%H:%M:%S')
    temp = kel_to_c(weather_data.get("temp"))
    fl = kel_to_c(weather_data.get("feels_like"))
    pressure = weather_data.get("pressure")
    humidity = weather_data.get("humidity")
    dew_point = weather_data.get("dew_point")
    uvi = weather_data.get("uvi")
    clouds = weather_data.get("clouds")
    visibility = weather_data.get('visibility')
    wind_speed = weather_data.get("wind_speed")
    rain_mm = weather_data.get("rain", {}).get("1h", 0) 
    description = weather_data.get("weather", [{}])[0].get("description", "")
    
    database.store_data(date, location.upper(), temp, fl, humidity, wind_speed, rain_mm)
    return(location.upper(), date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm, description)
    

def graph():
    type_of_trend = (input("what graph you want? temp/humidity/rain\n")).lower()
    if type_of_trend == "temp":
        (visual.temp_trend())
    elif type_of_trend == "humidity":
        (visual.humidity_trend())
    elif type_of_trend == "rain":
        (visual.rain_trend())
        
        
""" #whole running function for the whole systeme
running = True
#user_interface()
while running:
    user = (input("--> "))
    os.system('cls' if os.name == 'nt' else 'clear') # this function is used to clear the screen of the terminal
    print(user)
    if user == "help":
        user_interface()
    elif user == "exit":
        running = False
    elif user == "current":
        current_weather()
    elif user == "history":
        history()
    elif user == "trend":
        graph() 
        
        
            print("===============================")
    print("   Current Weather Report")
    print("===============================\n")    
    print(f"📍 Location: {location.upper()}, {country}")
    print(f"📅 Date: {date}\n")
    print(f"🌡️ Temperature : {temp} °C")
    print(f"🌡️ Feels like : {fl} °C")
    print(f"💧 Humidity    : {humidity} %")
    print(f"🌬️ Wind Speed  : {wind_speed} km/h")
    print(f"🌧️ Rain        : {rain_mm} mm\n")

        
        
        
        
        
        """