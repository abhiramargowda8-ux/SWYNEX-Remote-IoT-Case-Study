import csv
import random
from datetime import datetime, timedelta

OUTPUT_FILE = "sensor_data.csv"
NUMBER_OF_READINGS = 50

temperature = 25.0
humidity = 60.0

with open(OUTPUT_FILE, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "sensor_id",
        "temperature",
        "humidity"
    ])

    start_time = datetime.now()

    for i in range(NUMBER_OF_READINGS):
        temperature += random.uniform(-1.0, 1.0)
        humidity += random.uniform(-2.0, 2.0)

        writer.writerow([
            (start_time + timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M:%S"),
            "SENSOR-01",
            round(temperature, 2),
            round(humidity, 2)
        ])

print(f"Generated {NUMBER_OF_READINGS} simulated IoT readings.")
print(f"Data saved to {OUTPUT_FILE}")
