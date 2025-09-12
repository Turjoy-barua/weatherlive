from fetch import fetch_from_api
import datetime
def kel_to_c(kelvin):
    return (round(kelvin - 273.15, 1))
    

def user_interface():
    print('''========================================
        WEATHER ANALYZER - NSI
========================================
1. Current weather of a city
2. View saved weather history
3. Analyze weather trends
4. Visualize data with graphs
5. Exit''')
user_interface()
    
    
    
    
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
