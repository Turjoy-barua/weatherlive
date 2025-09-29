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
4. Visualize data with graphs -> graph !!! don't works !!!
5. Exit                       -> exit
''') # --> should erase the 4th option

def history():
    data =  database.read_data()
    for row in data:
        print(f"date : {row[1]}\tlocation : {row[2]}\ttemp : {row[3]}\tfeels_like : {row[4]}\thumidity : {row[5]}\twind : {row[6]}\train : {row[7]}")
    return 

def current_weather():
    location = (input("Enter your city : "))
    weather_data = fetch.fetch_from_api(location)
    temp = kel_to_c(weather_data.get("temp"))
    fl = kel_to_c(weather_data.get("feels_like"))
    humidity = weather_data.get("humidity")
    wind_speed = weather_data.get("wind_speed")
    rain_mm = weather_data.get("rain", {}).get("1h", 0) 
    date = datetime.datetime.fromtimestamp(weather_data.get("dt")).strftime('%Y-%m-%d %H:%M:%S')
    print("===============================")
    print("   Current Weather Report")
    print("===============================\n")    
    print(f"📍 Location: {location.upper()}")
    print(f"📅 Date: {date}\n")
    print(f"🌡️ Temperature : {temp} °C")
    print(f"🌡️ Feels like : {fl} °C")
    print(f"💧 Humidity    : {humidity} %")
    print(f"🌬️ Wind Speed  : {wind_speed} km/h")
    print(f"🌧️ Rain        : {rain_mm} mm\n")
    database.store_data(date, location.upper(), temp, fl, humidity, wind_speed, rain_mm)
    

def trend():
    type_of_trend = (input("what trend you want? temp/humidity/rain\n")).lower()
    num_of_days = int(input("of how many days?\n"))
    if type_of_trend == "temp":
        print(visual.temp_trend(num_of_days))
    elif type_of_trend == "humidity":
        print(visual.humidity_trend(num_of_days))
    elif type_of_trend == "rain":
        print(visual.rain_trend(num_of_days))
        
        
#whole running function for the whole systeme
running = True
user_interface()
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
        trend()