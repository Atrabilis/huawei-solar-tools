"""
EMI Data Retrieval Example

This script demonstrates how to use the `EMI` class from the `huawei_solar_tools` library to interact
with Huawei Energy Management Interface (EMI) devices. It retrieves data from the EMI, including all registers,
specific registers, and device-specific information, and saves detailed reports.

Features:
    - Connects to Huawei EMI devices via Modbus TCP.
    - Reads all registers and specific register values.
    - Saves reports for each EMI device in a structured directory.

Configuration:
    Environment variables are loaded from the `huawei_conf.env` file, which should include:
    - SMARTLOGGER_IP: IP address of the SmartLogger.
    - SMARTLOGGER_PORT: Port for Modbus communication.
    - EMI_IDS: Comma-separated list of EMI device IDs.

Dependencies:
    - python-dotenv
    - matplotlib
    - asyncio

Usage:
    1. Configure the `huawei_conf.env` file with the required connection details.
    2. Run the script:
        python emi_example.py

Output:
    - Text reports for each EMI device in the `emi_reports/` directory.
"""

import asyncio
import os
import matplotlib.pyplot as plt
import sys
from dotenv import load_dotenv
from huawei_solar_tools.devices.emi import EMI
import registers.emi_register_names as ern


async def main():
    """
    Main function to connect to Huawei EMI devices, retrieve data, and generate reports.
    """
    # Load environment variables
    load_dotenv("huawei_conf.env")
    host = os.getenv("SMARTLOGGER_IP")
    port = int(os.getenv("SMARTLOGGER_PORT"))
    emi_ids = [int(i) for i in os.getenv("EMI_IDS").split(",")]  # Support multiple EMI IDs

    for device_id in emi_ids:
        # Set up directories and report file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        reports_dir = os.path.join(script_dir, "emi_reports")
        os.makedirs(reports_dir, exist_ok=True)
        report_file = os.path.join(reports_dir, f"emi_{device_id}_report.txt")

        with open(report_file, "w") as report:
            sys.stdout = report  # Redirect output to the report file

            print(f"Connecting to EMI {device_id}...")

            # Initialize the EMI instance
            emi = EMI(host, port, device_id)

            try:
                # Connect to the EMI
                await emi.connect()
                print("Connection successful.")
                print(f"Is EMI {device_id} connected? {emi.is_connected()}")
                print(f"EMI ID: {emi.get_device_id()}")

                # Read and print all registers
                results = await emi.read_all_registers()
                print("All Registers:")
                for i in results:
                    print(i)

                # Read specific registers
                freq = await emi.read_raw_register(40031, 1)
                print(f"Grid Frequency: {freq[0] / 100} Hz")

                wind_speed = await emi.read_register_by_name(ern.WIND_SPEED)
                print(f"Wind Speed: {wind_speed}")

            except Exception as e:
                print(f"Error processing EMI {device_id}: {e}")

            finally:
                # Disconnect from the EMI
                emi.disconnect()
                print(f"Disconnected from EMI {device_id}.")


if __name__ == "__main__":
    asyncio.run(main())
