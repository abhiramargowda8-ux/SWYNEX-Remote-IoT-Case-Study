import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "data/sensor_data.csv"

data = pd.read_csv(DATA_FILE)

plt.figure(figsize=(10, 5))

plt.plot(
    data["timestamp"],
    data["temperature"],
    marker="o",
    label="Temperature (°C)"
)

plt.plot(
    data["timestamp"],
    data["humidity"],
    marker="o",
    label="Humidity (%)"
)

plt.xlabel("Time")
plt.ylabel("Reading")
plt.title("Remote IoT Sensor Monitoring")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("sensor_plot.png")

print("Visualization saved as sensor_plot.png")
