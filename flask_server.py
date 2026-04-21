from flask import Flask, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

def insert_data(value):
    conn = sqlite3.connect("Database/sensor_readings.db")
    c = conn.cursor()
    c.execute("INSERT INTO readings (value, time) VALUES (?, ?)",
              (value, datetime.now()))
    conn.commit()
    conn.close()

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    value = data['value']
    insert_data(value)
    return {"status": "ok"}

@app.route('/data', methods=['GET'])
def get_data():
    import sqlite3

    conn = sqlite3.connect("Database/sensor_readings.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT time, value 
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
            "time": datetime.fromisoformat(row[0]).isoformat(),
            "value": row[1]
        })

    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)