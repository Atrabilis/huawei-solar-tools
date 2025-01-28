"""
Inverter Data Retrieval Example

This script demonstrates how to use the `Inverter` class from the `huawei_solar_tools` library 
to interact with Huawei solar inverters. It retrieves various data points, including alarms, 
states, and characteristic curves, while saving detailed reports and plots.

Features:
    - Connects to Huawei inverters via Modbus TCP.
    - Retrieves all register data, specific registers, and interprets alarms and states.
    - Saves individual reports for each inverter.
    - Generates and saves plots for characteristic curves (cosφ-P/Pn, Q-U, PF-U).

Configuration:
    Environment variables are loaded from the `huawei_conf.env` file, which should include:
    - SMARTLOGGER_IP: IP address of the SmartLogger.
    - SMARTLOGGER_PORT: Port for Modbus communication.
    - INVERTER_IDS: Comma-separated list of inverter device IDs.

Dependencies:
    - python-dotenv
    - matplotlib
    - asyncio

Usage:
    1. Configure the `huawei_conf.env` file with the required connection details.
    2. Run the script:
        python inverter_example.py

Output:
    - Text reports for each inverter in the `inverter_reports/` directory.
    - Characteristic curve plots in the `plots/` directory.
"""

import asyncio
import os
import matplotlib.pyplot as plt
import sys
from dotenv import load_dotenv
from huawei_solar_tools.devices.inverter import Inverter
import huawei_solar_tools.registers.inverter_register_names as irn


async def main():
    """
    Main function to connect to Huawei inverters, retrieve data, and generate reports and plots.
    """
    # Load environment variables
    load_dotenv("huawei_conf.env")
    host = os.getenv("SMARTLOGGER_IP")
    port = int(os.getenv("SMARTLOGGER_PORT"))
    inverter_ids = [int(i) for i in os.getenv("INVERTER_IDS").split(",")]  # Support multiple inverter IDs

    for device_id in inverter_ids:
        # Set up directories and report file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        reports_dir = os.path.join(script_dir, "inverter_reports")
        os.makedirs(reports_dir, exist_ok=True)
        report_file = os.path.join(reports_dir, f"inverter_{device_id}_report.txt")

        with open(report_file, "w") as report:
            sys.stdout = report  # Redirect output to the report file

            print(f"Connecting to inverter {device_id}...")

            # Initialize the Inverter instance
            inverter = Inverter(host, port, device_id)

            try:
                # Connect to the inverter
                await inverter.connect()
                print("Connection successful.")
                print(f"Is inverter {device_id} connected? {inverter.is_connected()}")
                print(f"Inverter ID: {inverter.get_device_id()}")

                # Interpret alarms and states
                alarms = await inverter.interpret_alarms()
                print("Interpreted Alarms:")
                for alarm_type, alarm_details in alarms.items():
                    print(f"{alarm_type}: {alarm_details}")

                states = await inverter.interpret_states()
                print("Interpreted States:")
                print(states)

                # Read and print all registers
                results = await inverter.read_all_registers()
                print("All Registers:")
                for i in results:
                    print(i)

                # Read specific registers
                freq = await inverter.read_raw_register(32085, 1)
                print(f"Grid Frequency: {freq[0] / 100} Hz")

                serial_number = await inverter.read_register_by_name(irn.SN)
                print(f"Serial Number: {serial_number}")

                # Interpret and plot characteristic curves
                curve_1 = await inverter.interpret_cos_phi_p_pn_curve()
                curve_2 = await inverter.interpret_qu_curve()
                curve_3 = await inverter.interpret_pf_u_curve()

                plot_and_save_curve(curve_1, f"cosφ-P/Pn Curve (Inverter {device_id})", "P/Pn (%)", "cosφ", "P/Pn", "cosφ", f"cos_phi_p_pn_curve_{device_id}.png")
                plot_and_save_curve(curve_2, f"Q-U Curve (Inverter {device_id})", "U (%)", "Q (kVar)", "U", "Q", f"qu_curve_{device_id}.png")
                plot_and_save_curve(curve_3, f"PF-U Curve (Inverter {device_id})", "U (%)", "PF", "U", "PF", f"pf_u_curve_{device_id}.png")

                # Retrieve startup and shutdown times
                startup_time = await inverter.get_startup_time()
                print(f"Startup Time: {startup_time}")
                print(f"Startup Time (ISO): {await inverter.get_startup_time(iso=True)}")

                shutdown_time = await inverter.get_shutdown_time()
                print(f"Shutdown Time: {shutdown_time}")
                print(f"Shutdown Time (ISO): {await inverter.get_shutdown_time(iso=True)}")

                # Interpret grid code
                grid_code = await inverter.interpret_grid_code()
                print(f"Grid Code: {grid_code}")

            except Exception as e:
                print(f"Error processing inverter {device_id}: {e}")

            finally:
                # Disconnect from the inverter
                inverter.disconnect()
                print(f"Disconnected from inverter {device_id}.")


def plot_and_save_curve(curve, title, x_label, y_label, x_key, y_key, filename):
    """
    Plot and save a curve to the `plots/` directory.

    :param curve: List of dictionaries containing curve data.
    :param title: Title of the plot.
    :param x_label: Label for the X-axis.
    :param y_label: Label for the Y-axis.
    :param x_key: Key for X-axis data in the curve dictionary.
    :param y_key: Key for Y-axis data in the curve dictionary.
    :param filename: Filename to save the plot as.
    """
    if not curve:
        print(f"No data to plot for {title}.")
        return

    x = [point[x_key] for point in curve]
    y = [point[y_key] for point in curve]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', label=title)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Save the plot to the `plots/` directory
    plots_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(plots_dir, exist_ok=True)
    plot_path = os.path.join(plots_dir, filename)

    plt.savefig(plot_path)
    plt.close()
    print(f"Plot saved to: {plot_path}")


if __name__ == "__main__":
    asyncio.run(main())
