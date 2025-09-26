import sqlite3


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

def store_data(date, city, temp, feels_like, humidity, wind, rain):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather (date, city, temp, feels_like, humidity, wind, rain) VALUES (?, ?, ?, ?, ?, ?, ?)",
               (date, city, temp, feels_like, humidity, wind, rain))
    conn.commit()
    conn.close()
    
def read_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather")
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return (data)
