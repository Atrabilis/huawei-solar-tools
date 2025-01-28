"""
Huawei Solar System Data Collector

This script demonstrates how to collect data from various Huawei solar devices (inverters, batteries,
power meters, and EMIs) using the `huawei_solar_tools` library and store the data in ClickHouse
and InfluxDB databases for further analysis.

Devices:
    - Inverters
    - Batteries
    - Power Meters
    - EMI (Energy Management Interface)

Features:
    - Connects to Huawei solar devices via Modbus TCP.
    - Reads all registers from each device.
    - Stores collected data in ClickHouse and InfluxDB for analysis and visualization.

Configuration:
    Environment variables are loaded from `huawei_conf.env`. The file should include:
    - Device connection details (e.g., IP, port, device IDs).
    - Database connection details for ClickHouse and InfluxDB.

Dependencies:
    - python-dotenv
    - clickhouse-connect
    - influxdb-client
    - asyncio

Usage:
    1. Configure the `huawei_conf.env` file with the required connection details.
    2. Run the script:
        python huawei_data_collector.py

    Example `huawei_conf.env`:
        SMARTLOGGER_IP=192.168.1.100
        SMARTLOGGER_PORT=502
        INVERTER_IDS=1,2
        BATTERY_IDS=3,4
        POWER_METER_IDS=5,6
        EMI_IDS=7,8
        INFLUXDB_URL_UA=http://localhost:8086
        INFLUXDB_TOKEN_UA=your_influxdb_token
        INFLUXDB_ORG_UA=your_org
        INFLUXDB_BUCKET_UA=solar_data
        HOST_CLICKHOUSE=localhost
        PORT_CLICKHOUSE=9000
        USER_CLICKHOUSE=default
        PASSWORD_CLICKHOUSE=your_password
        TABLE_CLICKHOUSE=solar_data

Output:
    - Data from all devices is written to ClickHouse and InfluxDB.
    - Prints connection and processing status to the console.
"""

import os
import asyncio
from datetime import datetime, timezone
from dotenv import load_dotenv, find_dotenv
from clickhouse_connect import get_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from huawei_solar_tools.devices.inverter import Inverter
from huawei_solar_tools.devices.battery import Battery
from huawei_solar_tools.devices.power_meter import PowerMeter
from huawei_solar_tools.devices.emi import EMI

async def main():
    """
    Main function to collect data from Huawei devices and store it in databases.
    """
    clickhouse_client = None
    influx_client = None
    data_clickhouse = []
    points_influx = []

    # Create ClickHouse client
    print("Creating ClickHouse client...")
    try:
        clickhouse_client = get_client(
            host=clickhouse_host,
            port=clickhouse_port,
            user=clickhouse_user,
            password=clickhouse_password
        )
    except Exception as e:
        print(f"Error creating ClickHouse client: {e}")

    # Create InfluxDB client
    print("Creating InfluxDB client...")
    try:
        influx_client = InfluxDBClient(
            url=influxdb_url_ua,
            token=influxdb_token_ua,
            org=influxdb_org_ua
        )
        influx_write_api = influx_client.write_api(write_options=SYNCHRONOUS)
    except Exception as e:
        print(f"Error creating InfluxDB client: {e}")

    # Fetch data from each type of device
    devices = {
        "inverter": (inverter_ids, Inverter),
        "battery": (battery_ids, Battery),
        "power_meter": (power_meter_ids, PowerMeter),
        "emi": (emi_ids, EMI)
    }

    for device_type, (device_ids, DeviceClass) in devices.items():
        for device_id in device_ids:
            try:
                # Initialize and connect to the device
                device = DeviceClass(host, port, device_id)
                await device.connect()

                # Fetch all registers and prepare data for databases
                results = await device.read_all_registers()
                data_clickhouse.extend([
                    (stamptime, device_type, device_id, result[0], result[1])
                    for result in results if isinstance(result[1], float)
                ])
                points_influx.extend([
                    Point("huawei_solar_system")
                    .tag(f"{device_type}_id", device_id)
                    .field(result[0], result[1])
                    .time(stamptime, WritePrecision.S)
                    for result in results if isinstance(result[1], float)
                ])
                device.disconnect()
            except Exception as e:
                print(f"Error processing {device_type} {device_id}: {e}")

    # Write data to ClickHouse
    if clickhouse_client and data_clickhouse:
        clickhouse_client.insert(clickhouse_table, data_clickhouse)
        print(f"Data written to ClickHouse.")

    # Write data to InfluxDB
    if influx_write_api and points_influx:
        influx_write_api.write(bucket=influxdb_bucket_ua, record=points_influx)
        print(f"Data written to InfluxDB.")

    # Close database clients
    if influx_client:
        influx_client.close()
    if clickhouse_client:
        clickhouse_client.close()


if __name__ == "__main__":
    # Load environment variables
    load_dotenv(find_dotenv("huawei_conf.env"))

    # Environment variables
    host = os.getenv("SMARTLOGGER_IP")
    port = int(os.getenv("SMARTLOGGER_PORT"))
    inverter_ids = [int(i) for i in os.getenv("INVERTER_IDS", "").split(",")]
    battery_ids = [int(i) for i in os.getenv("BATTERY_IDS", "").split(",")]
    power_meter_ids = [int(i) for i in os.getenv("POWER_METER_IDS", "").split(",")]
    emi_ids = [int(i) for i in os.getenv("EMI_IDS", "").split(",")]

    # InfluxDB configuration
    influxdb_url_ua = os.getenv("INFLUXDB_URL_UA")
    influxdb_token_ua = os.getenv("INFLUXDB_TOKEN_UA")
    influxdb_org_ua = os.getenv("INFLUXDB_ORG_UA")
    influxdb_bucket_ua = os.getenv("INFLUXDB_BUCKET_UA")

    # ClickHouse configuration
    clickhouse_host = os.getenv("HOST_CLICKHOUSE")
    clickhouse_port = int(os.getenv("PORT_CLICKHOUSE"))
    clickhouse_user = os.getenv("USER_CLICKHOUSE")
    clickhouse_password = os.getenv("PASSWORD_CLICKHOUSE")
    clickhouse_table = os.getenv("TABLE_CLICKHOUSE")

    # Current timestamp
    stamptime = datetime.now(timezone.utc).replace(second=0, microsecond=0)

    asyncio.run(main())
