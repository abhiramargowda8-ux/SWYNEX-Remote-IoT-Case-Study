# Remote IoT Architecture

## Architecture Diagram

```text
+----------------------+
|  Simulated IoT       |
|      Sensors         |
+----------+-----------+
           |
           v
+----------------------+
| Data Generation      |
|      Python          |
+----------+-----------+
           |
           v
+----------------------+
| CSV Data Storage     |
+----------+-----------+
           |
           v
+----------------------+
| Data Processing      |
|      Pandas          |
+----------+-----------+
           |
           v
+----------------------+
| Visualization        |
|     Matplotlib       |
+----------+-----------+
           |
           v
+----------------------+
| Alert Rule           |
| Temperature > Limit  |
+----------+-----------+
           |
           v
+----------------------+
| Monitoring /         |
| Notification         |
+----------------------+

## Data Flow

1. Simulated sensors generate readings.
2. Python records the readings.
3. Data is stored in CSV format.
4. Pandas processes the data.
5. Matplotlib visualizes the readings.
6. An alert rule checks the temperature.
7. The system identifies readings that exceed the configured threshold.
