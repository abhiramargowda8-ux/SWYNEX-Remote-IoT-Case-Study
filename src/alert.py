import pandas as pd

DATA_FILE = "data/sensor_data.csv"
TEMPERATURE_THRESHOLD = 30.0

data = pd.read_csv(DATA_FILE)

alerts = data[data["temperature"] > TEMPERATURE_THRESHOLD]

if alerts.empty:
    print("No temperature alerts detected.")
else:
    print("Temperature alerts detected:")

    for _, row in alerts.iterrows():
        print(
            f"ALERT | {row['timestamp']} | "
            f"{row['sensor_id']} | "
            f"Temperature: {row['temperature']} °C"
        )
