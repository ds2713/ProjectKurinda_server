from flask import Flask, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

def insert_data(value):
    conn = sqlite3.connect("Database/sensor_readings.db")
    # dt = datetime.fromisoformat(datetime.now().isoformat())
    dt = datetime.now().isoformat()
    # timestamp_ms = int(dt.timestamp() * 1000)
    c = conn.cursor()
    c.execute("INSERT INTO readings (site_id, temperature, acceleration, soil_moisture, time) VALUES (?, ?, ?, ?, ?)",
              (value['site_id'], value['temperature'], value['acceleration'], value['soil_moisture'], dt))
    conn.commit()
    conn.close()

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    site_id = data['site_id']
    temperature = data['temperature']
    acceleration = data['acceleration']
    soil_moisture = data['soil_moisture']
    insert_data({
        'site_id': site_id,
        'temperature': temperature,
        'acceleration': acceleration,
        'soil_moisture': soil_moisture
    })
    return {"status": "ok"}

@app.route('/acceleration', methods=['GET'])
def get_acceleration():
    import sqlite3
    from collections import defaultdict

    conn = sqlite3.connect("Database/sensor_readings.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT site_id, time, acceleration
        FROM readings
        ORDER BY time ASC
    """)

    rows = cursor.fetchall()
    conn.close()

    series = defaultdict(list)

    for site_id, time, acceleration in rows:
        series[site_id].append({
            "time": time,
            "acceleration": acceleration
        })

    # Convert to Grafana-friendly format
    result = []
    for site_id, datapoints in series.items():
        result.append({
            "target": f"site_{site_id}",
            "datapoints": [
                [point["acceleration"], point["time"]] for point in datapoints
            ]
        })

    return result

@app.route('/data', methods=['GET'])
def get_data():
    import sqlite3

    conn = sqlite3.connect("Database/sensor_readings.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT time, site_id, temperature, acceleration, soil_moisture 
        FROM readings 
        ORDER BY time ASC
        LIMIT 100
    """)

    rows = cursor.fetchall()
    conn.close()

    # Convert to JSON format Grafana understands
    result = []
    for row in rows:
        result.append({
            # "time": datetime.fromisoformat(row[0]).isoformat(),
            "time": row[0],
            "site_id": row[1],
            "temperature": row[2],
            "acceleration": row[3],
            "soil_moisture": row[4]
        })

    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)