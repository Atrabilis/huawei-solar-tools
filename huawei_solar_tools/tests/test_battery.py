"""
Battery Interaction Example

This script demonstrates how to use the `Battery` class from the `huawei_solar_tools` library.
It connects to specified Huawei battery devices, retrieves information such as system status, 
working modes, and registers, and saves a detailed report for each battery.

Additionally, the script includes functionality to plot and save characteristic curves.

Usage:
    1. Configure the `huawei_conf.env` file with the necessary environment variables:
        - SMARTLOGGER_IP: IP address of the SmartLogger.
        - SMARTLOGGER_PORT: Port for Modbus communication.
        - BATTERY_IDS: Comma-separated list of battery IDs.
    2. Run the script:
        python battery_example.py

Dependencies:
    - matplotlib
    - python-dotenv
    - asyncio

Output:
    - Text reports for each battery in the `battery_reports/` directory.
    - Saved plots in the `plots/` directory.
"""

import asyncio
import os
import matplotlib.pyplot as plt
import sys
from dotenv import load_dotenv
from huawei_solar_tools.devices.battery import Battery
import huawei_solar_tools.registers.battery_register_names as brn


async def main():
    """
    Main function to connect to Huawei batteries, retrieve data, and generate reports.
    """
    # Load environment variables
    load_dotenv("huawei_conf.env")
    host = os.getenv("SMARTLOGGER_IP")
    port = int(os.getenv("SMARTLOGGER_PORT"))
    battery_ids = [int(i) for i in os.getenv("BATTERY_IDS").split(",")]

    for device_id in battery_ids:
        # Set up directories and report file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        reports_dir = os.path.join(script_dir, "battery_reports")
        os.makedirs(reports_dir, exist_ok=True)
        report_file = os.path.join(reports_dir, f"battery_{device_id}_report.txt")

        with open(report_file, "w") as report:
            sys.stdout = report  # Redirect output to the report file

            print(f"Connecting to battery {device_id}...")

            # Initialize the Battery instance
            battery = Battery(host, port, device_id)

            try:
                # Connect to the battery
                await battery.connect()
                print("Connection successful.")
                print(f"Is battery {device_id} connected? {battery.is_connected()}")
                print(f"Battery ID: {battery.get_device_id()}")

                # Read and print all registers
                results = await battery.read_all_registers()
                print("All Registers:")
                for i in results:
                    print(i)

                # Read specific registers
                freq = await battery.read_raw_register(37700, 10)
                print(f"Grid Frequency: {freq[0] / 100} Hz")

                serial_number = await battery.read_register_by_name(brn.ENERGY_STORAGE_SOC)
                print(f"Serial Number: {serial_number}")

                # Retrieve system and unit statuses
                print(await battery.get_unit_status())
                print(await battery.get_system_status())

                # Retrieve working mode and product mode
                working_mode = await battery.get_working_mode()
                print(f"Working Mode: {working_mode}")

                product_mode = await battery.get_product_mode()
                print(f"Product Mode: {product_mode}")

            except Exception as e:
                print(f"Error processing battery {device_id}: {e}")

            finally:
                # Disconnect from the battery
                battery.disconnect()
                print(f"Disconnected from battery {device_id}.")

if __name__ == "__main__":
    asyncio.run(main())
