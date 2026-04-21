import sqlite3

conn = sqlite3.connect("Database/sensor_readings.db")
cursor = conn.cursor()

cursor.execute("SELECT id, value, time FROM readings ORDER BY time")

rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Value: {row[1]}, Time: {row[2]}")

conn.close()