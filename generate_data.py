import requests
import random
import time

URL = "http://127.0.0.1:5000/data"  # change if needed

while True:
    value = random.uniform(20, 30)  # random float

    data = {
        "value": value
    }

    try:
        r = requests.post(URL, json=data)
        print("Sent:", data, "Response:", r.status_code)
    except Exception as e:
        print("Error:", e)

    time.sleep(5)  # send every 5 seconds#