import sqlite3
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    temp REAL,
    humidity INTEGER,
    wind REAL,
    rain REAL
)
""")
cursor.execute("INSERT INTO weather (date, temp, humidity, wind, rain) VALUES (?, ?, ?, ?, ?)",
               ("2025-09-12", 25, 65, 12, 0))

conn.commit()
conn.close()