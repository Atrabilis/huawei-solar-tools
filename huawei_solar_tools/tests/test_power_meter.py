"""
Power Meter Data Retrieval Example

This script demonstrates how to use the `PowerMeter` class from the `huawei_solar_tools` library 
to interact with Huawei power meters. It retrieves various data points, including all registers 
and specific register values, and saves detailed reports.

Features:
    - Connects to Huawei power meters via Modbus TCP.
    - Retrieves all register data and specific register values (e.g., power factor, grid frequency).
    - Saves individual reports for each power meter.

Configuration:
    Environment variables are loaded from the `huawei_conf.env` file, which should include:
    - SMARTLOGGER_IP: IP address of the SmartLogger.
    - SMARTLOGGER_PORT: Port for Modbus communication.
    - POWER_METER_IDS: Comma-separated list of power meter device IDs.

Dependencies:
    - python-dotenv
    - asyncio

Usage:
    1. Configure the `huawei_conf.env` file with the required connection details.
    2. Run the script:
        python power_meter_example.py

Output:
    - Text reports for each power meter in the `power_meter_reports/` directory.
"""

import asyncio
import os
import sys
from dotenv import load_dotenv
from huawei_solar_tools.devices.power_meter import PowerMeter
import huawei_solar_tools.registers.power_meter_register_names as pmrn


async def main():
    """
    Main function to connect to Huawei power meters, retrieve data, and generate reports.
    """
    # Load environment variables
    load_dotenv("huawei_conf.env")
    host = os.getenv("SMARTLOGGER_IP")
    port = int(os.getenv("SMARTLOGGER_PORT"))
    meter_ids = [int(i) for i in os.getenv("POWER_METER_IDS").split(",")]

    for device_id in meter_ids:
        # Set up directories and report file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        reports_dir = os.path.join(script_dir, "power_meter_reports")
        os.makedirs(reports_dir, exist_ok=True)
        report_file = os.path.join(reports_dir, f"power_meter_{device_id}_report.txt")

        with open(report_file, "w") as report:
            sys.stdout = report  # Redirect output to the report file

            print(f"Connecting to Power Meter {device_id}...")

            # Initialize the PowerMeter instance
            power_meter = PowerMeter(host, port, device_id)

            try:
                # Connect to the power meter
                await power_meter.connect()
                print("Connection successful.")
                print(f"Is Power Meter {device_id} connected? {power_meter.is_connected()}")
                print(f"Power Meter ID: {power_meter.get_device_id()}")

                # Read and print all registers
                results = await power_meter.read_all_registers()
                print("All Registers:")
                for i in results:
                    print(i)

                # Read specific registers
                freq = await power_meter.read_raw_register(32284, 1)
                print(f"Grid Frequency: {freq[0] / 100} Hz")

                power_factor = await power_meter.read_register_by_name(pmrn.POWER_FACTOR)
                print(f"Power Factor: {power_factor}")

            except Exception as e:
                print(f"Error processing Power Meter {device_id}: {e}")

            finally:
                # Disconnect from the power meter
                power_meter.disconnect()
                print(f"Disconnected from Power Meter {device_id}.")


if __name__ == "__main__":
    asyncio.run(main())
