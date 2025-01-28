"""
Meter Data Retrieval Example

This script demonstrates how to use the `Meter` class from the `huawei_solar_tools` library 
to interact with Huawei power meters. It retrieves various data points, including all registers 
and specific register values, while saving detailed reports.

Features:
    - Connects to Huawei power meters via Modbus TCP.
    - Retrieves all register data and specific register values (e.g., Meter Status, Grid Frequency).
    - Saves individual reports for each meter.

Configuration:
    Environment variables are loaded from the `huawei_conf.env` file, which should include:
    - SMARTLOGGER_IP: IP address of the SmartLogger.
    - SMARTLOGGER_PORT: Port for Modbus communication.
    - METER_IDS: Comma-separated list of meter device IDs.

Dependencies:
    - python-dotenv
    - asyncio

Usage:
    1. Configure the `huawei_conf.env` file with the required connection details.
    2. Run the script:
        python meter_example.py

Output:
    - Text reports for each meter in the `meter_reports/` directory.
"""

import asyncio
import os
import sys
from dotenv import load_dotenv
from huawei_solar_tools.devices.meter import Meter
import huawei_solar_tools.registers.meter_register_names as mrn


async def main():
    """
    Main function to connect to Huawei power meters, retrieve data, and generate reports.
    """
    # Load environment variables
    load_dotenv("huawei_conf.env")
    host = os.getenv("SMARTLOGGER_IP")
    port = int(os.getenv("SMARTLOGGER_PORT"))
    meter_ids = [int(i) for i in os.getenv("METER_IDS").split(",")]

    for device_id in meter_ids:
        # Set up directories and report file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        reports_dir = os.path.join(script_dir, "meter_reports")
        os.makedirs(reports_dir, exist_ok=True)
        report_file = os.path.join(reports_dir, f"meter_{device_id}_report.txt")

        with open(report_file, "w") as report:
            sys.stdout = report  # Redirect output to the report file

            print(f"Connecting to meter {device_id}...")

            # Initialize the Meter instance
            meter = Meter(host, port, device_id)

            try:
                # Connect to the meter
                await meter.connect()
                print("Connection successful.")
                print(f"Is Meter {device_id} connected? {meter.is_connected()}")
                print(f"Meter ID: {meter.get_device_id()}")

                # Read and print all registers
                results = await meter.read_all_registers()
                print("All Registers:")
                for i in results:
                    print(i)

                # Read specific registers
                freq = await meter.read_raw_register(37118, 1)
                print(f"Grid Frequency: {freq[0] / 100} Hz")

                meter_status = await meter.read_register_by_name(mrn.METER_STATUS)
                print(f"Meter Status: {meter_status}")

            except Exception as e:
                print(f"Error processing Meter {device_id}: {e}")

            finally:
                # Disconnect from the meter
                meter.disconnect()
                print(f"Disconnected from Meter {device_id}.")


if __name__ == "__main__":
    asyncio.run(main())
