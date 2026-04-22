# GLOC Server

## Python Script Overview

- **flask_server.py**: Main Flask API server. Receives sensor data via HTTP POST requests and stores it in the SQLite database (`Database/sensor_readings.db`). Provides endpoints for retrieving sensor data (e.g., acceleration).

- **generate_data.py**: Simulates sensor data by generating random values and sending them to the Flask server's `/data` endpoint. Useful for testing the server and database.

- **initialise_database.py**: Creates the `Data/sensor_readings` table in the SQLite database. Run this script before starting the server to initialize the database schema.

- **print_database.py**: Prints all entries in the `Data/sensor_readings` table, displaying the stored sensor data for inspection or debugging.

## Workspace Setup (using UV)

1. **Install [UV](https://github.com/astral-sh/uv):**
	- Follow the instructions in the UV documentation to install UV for your platform.

2. **Install dependencies:**
	- In the project root, run:
	  ```sh
	  uv pip install -r pyproject.toml
	  ```
	  or, if using PEP 621/modern projects:
	  ```sh
	  uv pip install .
	  ```

3. **Create and initialize the database:**
	- Run:
	  ```sh
	  uv run initialise_database.py
	  ```

4. **Start the Flask server:**
	- Run:
	  ```sh
	  uv run flask_server.py
	  ```

5. **(Optional) Generate test data:**
	- In a separate terminal, run:
	  ```sh
	  uv run generate_data.py
	  ```

## Interfacing with Grafana

1. **Configure Grafana Data Source:**
	- Use the [SQLite](https://grafana.com/grafana/plugins/fr-ser-sqlite-datasource/) or [InfluxDB](https://grafana.com/grafana/plugins/influxdata-influxdb-datasource/) plugin, depending on your setup.
	- For SQLite: Point the data source to `Database/sensor_readings.db`.
	- For InfluxDB: If you export or mirror data to InfluxDB, configure the connection accordingly.

2. **Create Dashboards:**
	- Use Grafana's query editor to visualize tables or time series from the `readings` table (site_id, temperature, acceleration, soil_moisture, time).

3. **Example Query (SQLite):**
	```sql
	SELECT time, temperature, acceleration, soil_moisture FROM readings WHERE site_id = 1 ORDER BY time DESC
	```

4. **Authentication:**
	- Ensure Grafana has read access to the database file. For production, consider exporting data to a dedicated time-series database (e.g., InfluxDB) for better performance and concurrency.

---
For more details, see the code comments in each script.
