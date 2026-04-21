import sqlite3

conn = sqlite3.connect("Database/sensor_readings.db")
c = conn.cursor()

c.execute("""
CREATE TABLE readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value REAL,
    time TIMESTAMP
)
""")

conn.commit()
conn.close()