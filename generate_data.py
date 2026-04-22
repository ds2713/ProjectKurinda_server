import requests
import random
import time

URL = "http://127.0.0.1:5000/data"  # change if needed

while True:
    site_id = random.randint(1, 5)  # random site ID between 1 and 5
    temperature = random.uniform(0, 45)  # random temperature
    acceleration = random.uniform(-10, 10)  # random acceleration
    soil_moisture = random.uniform(0, 100)  # random soil moisture

    data = {
        "site_id": site_id,
        "temperature": temperature,
        "acceleration": acceleration,
        "soil_moisture": soil_moisture
    }

    try:
        r = requests.post(URL, json=data)
        print("Sent:", data, "Response:", r.status_code)
    except Exception as e:
        print("Error:", e)

    time.sleep(0.1)  # send every 5 seconds#