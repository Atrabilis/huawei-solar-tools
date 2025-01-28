"""
Battery Module

This module defines the `Battery` class, which extends the `Device` class to handle
Huawei Energy Storage Unit (ESU) functionalities using Modbus communication. The
class is tailored to interact with battery-specific registers and provides methods
to retrieve operational data as described in Huawei's technical documentation.

Classes:
    - Battery: Represents an energy storage unit and provides methods to interact
      with its operational states, system status, working mode, and product model.

Usage:
    The `Battery` class can be instantiated with the IP address, port, and slave ID
    of the Huawei energy storage system. It provides asynchronous methods to query
    specific battery attributes.

Example:
    from huawei_solar_tools.devices.battery import Battery

    async def main():
        battery = Battery("192.168.1.100", 502, 1)
        status = await battery.get_unit_status()
        print(status)
"""

from huawei_solar_tools.devices.device import Device
from huawei_solar_tools.registers.battery_registers import battery_registers
class Battery(Device):
    """
    Clase Battery que hereda de Device.
    Diseñada para manejar funcionalidades específicas de las baterías según el manual Huawei.
    """
    def __init__(self, host, port, slave_id):
        """
        Inicializa la clase Battery con los parámetros básicos para comunicación Modbus.

        :param host: Dirección IP del dispositivo.
        :param port: Puerto del dispositivo.
        :param slave_id: ID del dispositivo esclavo Modbus.
        """
        super().__init__(host, port, slave_id, battery_registers)
    
    async def get_unit_status(self):
        """
        Retrieve the operational status of up to two Energy Storage Units (ESUs).

        Each ESU status is retrieved from its specific Modbus register and mapped
        to a human-readable description.

        :return: Dictionary with unit IDs as keys and their operational status as values.
        :rtype: dict
        :raises RuntimeError: If the status retrieval process fails.
        """
        
        try:
            unit_statuses = {}

            # Define the registers for the two units
            unit_registers = {
                1: 37000,  # Register for ESU 1
                2: 37741   # Register for ESU 2
            }

            # Status mappings
            status_mapping = {
                0: "Offline",
                1: "Standby",
                2: "Running",
                3: "Fault",
                4: "Sleep mode"
            }

            # Loop through each unit and read its status
            for unit_id, register in unit_registers.items():
                try:
                    # Read the register value
                    raw_status = await self.read_raw_register(register, 1)
                    raw_status = raw_status[0]
                    # Map the status to its description
                    unit_statuses[unit_id] = status_mapping.get(raw_status, "Unknown")
                except Exception as e:
                    unit_statuses[unit_id] = f"Error: {e}"

            return unit_statuses

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve unit statuses: {e}")

    async def get_system_status(self):
        """
        Retrieve the overall operational status of the energy storage system.

        The system status is obtained from a specific Modbus register and mapped
        to a human-readable description.

        :return: String representing the system's operational status.
        :rtype: str
        :raises RuntimeError: If the system status retrieval process fails.
        """
        
        try:
            # Register for the general system running status
            system_status_register = 37762

            # Status mappings
            status_mapping = {
                0: "Offline",
                1: "Standby",
                2: "Running",
                3: "Fault",
                4: "Sleep mode"
            }

            # Read the register value
            raw_status = await self.read_raw_register(system_status_register, 1)
            raw_status = raw_status[0]
            # Map the status to its description
            return status_mapping.get(raw_status, "Unknown")

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve system status: {e}")
        
    async def get_working_mode(self):
        """
        Retrieve the working mode of the energy storage system.

        The working mode indicates how the system is currently configured to manage
        energy storage and usage. The mode is determined based on a Modbus register value.

        :return: String representing the system's working mode.
        :rtype: str
        :raises RuntimeError: If the working mode retrieval process fails.
        """

        try:
            # Register for the working mode
            working_mode_register = 37006

            # Working mode mappings
            working_mode_mapping = {
                0: "None",
                1: "Forced charge/discharge",
                2: "Time of Use (LG)",
                3: "Fixed charge/discharge",
                4: "Maximise self-consumption",
                5: "Fully fed to grid",
                6: "Time of Use (LUNA2000)",
                7: "Remote scheduling - Maximise self-use",
                8: "Remote scheduling - Fully fed to grid",
                9: "Remote scheduling - TOU",
                10: "AI energy management and scheduling"
            }

            # Read the register value
            raw_mode = await self.read_raw_register(working_mode_register, 1)
            raw_mode = raw_mode[0]
            # Map the mode to its description
            return working_mode_mapping.get(raw_mode, "Unknown")

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve working mode: {e}")

    async def get_product_mode(self):
        """
        Retrieve the product model of the energy storage system.

        The product model indicates the specific hardware being used (e.g., LUNA2000 or LG-RESU).
        The model is determined from a Modbus register value.

        :return: String representing the product model.
        :rtype: str
        :raises RuntimeError: If the product model retrieval process fails.
        """

        try:
            # Register for the product model
            product_model_register = 47000

            # Product model mappings
            product_mode_mapping = {
                0: "None",
                1: "LG-RESU",
                2: "Huawei-LUNA2000"
            }

            # Read the register value
            raw_mode = await self.read_raw_register(product_model_register, 1)
            raw_mode = raw_mode[0]
            # Map the model to its description
            return product_mode_mapping.get(raw_mode, "Unknown")

        except Exception as e:
            raise RuntimeError(f"Failed to retrieve product mode: {e}")