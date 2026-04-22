import sqlite3

conn = sqlite3.connect("Database/sensor_readings.db")
cursor = conn.cursor()

cursor.execute("SELECT id, site_id, temperature, acceleration, soil_moisture, time FROM readings ORDER BY time")

rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Site ID: {row[1]}, Temperature: {row[2]}, Acceleration: {row[3]}, Soil Moisture: {row[4]}, Time: {row[5]}")

conn.close()