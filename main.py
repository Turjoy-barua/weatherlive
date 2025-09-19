from fetch import fetch_from_api
import datetime
import time
import os 
def kel_to_c(kelvin):
    return (round(kelvin - 273.15, 1))
    

def user_interface():
    print('''========================================
        WEATHER ANALYZER - NSI
========================================
1. Current weather of a city  -> current
2. View saved weather history -> history
3. Analyze weather trends     -> trend
4. Visualize data with graphs -> graph
5. Exit                       -> exit
''')

    
    
    
    
def current_weather():
    weather_data = fetch_from_api()
    temp = kel_to_c(weather_data.get("temp"))
    fl = kel_to_c(weather_data.get("feels_like"))
    humidity = weather_data.get("humidity")
    wind_speed = weather_data.get("wind_speed")
    rain_mm = weather_data.get("rain", {}).get("1h", 0) 
    date = datetime.datetime.fromtimestamp(weather_data.get("dt")).strftime('%Y-%m-%d %H:%M:%S')
    print("===============================")
    print("   Current Weather Report")
    print("===============================\n")
    
    print(f"📍 Location: paris")
    print(f"📅 Date: {date}\n")
    print(f"🌡️ Temperature : {temp} °C")
    print(f"🌡️ Feels like : {fl} °C")
    print(f"💧 Humidity    : {humidity} %")
    print(f"🌬️ Wind Speed  : {wind_speed} km/h")
    print(f"🌧️ Rain        : {rain_mm} mm\n")
    
    # print("Data successfully saved to database ✅")


#whole running function for the whole systeme
running = True
while running:
    user = input()
    if user.lower() == "exit":
        running = False
    #elif user.lower() == "help":
    os.system('cls' if os.name == 'nt' else 'clear') # this function is used to clear the screen of the terminal 
    