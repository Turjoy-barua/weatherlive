import sqlite3
from supabase import create_client, Client


""" 
# --> used to save online 
def store_data_supabase(location, country, date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm, description, total_daytime):
    data = {"Location": location, "country" :country, "date" : date, "sunrise" : sunrise, "sunset" : sunset, "temp" : temp, "fl" : fl, "pressure" : pressure, "humidity" : humidity, "dew point" : dew_point, "uvi" : uvi, "clouds" : clouds, "visibility" : visibility, "wind speed" : wind_speed, "rain" : rain_mm,  "description" : description, "total daytime" : total_daytime}

    url = "https://sixaahscbcfesarjxdgf.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNpeGFhaHNjYmNmZXNhcmp4ZGdmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjAxOTY1NTgsImV4cCI6MjA3NTc3MjU1OH0.Z88M-sHfacc4hozYLSLyYo3557nh5AW02496YdsUopI"
    supabase: Client = create_client(url, key)
    database_response = supabase.table("weather datasheet").insert(data).execute()

        
 """
  
# --> used for local data
def initializing():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT,
        country TEXT,
        date TEXT,
        sunrise TEXT,
        sunset TEXT,
        temp REAL,
        feels_like REAL,
        pressure REAL,
        humidity INTEGER,
        dew_point REAL,
        uvi REAL,
        clouds INTEGER,
        visibility REAL,
        wind_speed REAL,
        rain_mm REAL,
        description TEXT,
        total_daytime REAL
    )
    """)
    conn.commit()
    conn.close()

def store_data_local(location, country, date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm, description, total_daytime):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather (location, country, date, sunrise, sunset, temp, feels_like, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm, description, total_daytime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (location, country, date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm, description, total_daytime))
    conn.commit()
    conn.close()


#store_data_local("PARIS", "France", 2025-10-14, "08:09:23", "19:03:42", 13.0, 12.5, 1026, 82, 10.0, 0, 100, 10.0, 5.14, 0, "overcast clouds", 39259.0 )    

def read_data(): # --> isn't used in the web interface
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather")
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return (data)

