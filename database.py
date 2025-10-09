import sqlite3
import pa

def initializing():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        city TEXT,
        temp REAL,
        feels_like REAL,
        humidity INTEGER,
        wind REAL,
        rain REAL
    )
    """)
    conn.commit()
    conn.close()

def store_data(location, country, date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm, description, total_daytime):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather (location.upper(), country, date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm, description, total_daytime) VALUES (?, ?, ?, ?, ?, ?, ?)",
               (location.upper(), country, date, sunrise, sunset, temp, fl, pressure, humidity, dew_point, uvi, clouds, visibility, wind_speed, rain_mm, description, total_daytime))
    conn.commit()
    conn.close()
    print("Data successfully saved to database ✅")
    
def read_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather")
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return (data)

print(read_data())
def data_frame():
    df = pd
    
    pass