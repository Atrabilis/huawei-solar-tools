from huawei_solar_tools.utils.connection import create_modbus_tcp_client
from huawei_solar_tools.utils.register_interpreter import convert_registers_to_readable


class Device:
    """
    Device Module

    This module defines the `Device` class, which serves as a base for all Huawei solar devices. 
    It provides core functionalities for Modbus TCP communication and register operations, 
    allowing derived classes to focus on device-specific features.

    Classes:
        - Device: Base class for managing Modbus communication and interacting with device registers.

    Usage:
        The `Device` class is intended to be extended by specific device classes, such as inverters or batteries.
        It handles connection management, register operations, and common device functionalities.

    Example:
        from huawei_solar_tools.devices.device import Device

        async def main():
            device = Device("192.168.1.100", 502, 1, registers)
            await device.connect()
            register_value = await device.read_register_by_name("some_register_name")
            print(register_value)
            device.disconnect()
    """
    
    def __init__(self, host, port, device_id, registers):
        """
        Initialize the device.

        :param host: IP address of the Modbus server.
        :type host: str
        :param port: Port of the Modbus server.
        :type port: int
        :param device_id: Modbus unit ID of the device.
        :type device_id: int
        :param registers: Dictionary of register mappings for the device.
        :type registers: dict
        """

        self.host = host
        self.port = port
        self.device_id = device_id
        self.registers = registers
        self.client = None

    async def connect(self):
        """
        Establish a Modbus TCP connection.

        :raises ConnectionError: If the connection to the device fails.
        """

        self.client = await create_modbus_tcp_client(self.host, self.port, self.device_id)
        if not self.client:
            raise ConnectionError(f"Failed to connect to device {self.device_id} at {self.host}:{self.port}")

    def disconnect(self):
        """
        Close the Modbus TCP connection.
        """

        if self.client:
            self.client.close()
            self.client = None

    async def read_register_by_name(self, name):
        """
        Read a register by its name.

        :param name: Name of the register to read.
        :type name: str
        :return: Decoded value of the register.
        :rtype: Any
        :raises ValueError: If the register name is not found in the mappings.
        :raises ConnectionError: If the device is not connected.
        :raises RuntimeError: If there is an error while reading the register.
        """

        if name not in self.registers:
            raise ValueError(f"Register '{name}' not found in device register mappings.")

        reg_info = self.registers[name]
        address = reg_info['address']
        quantity = reg_info['quantity']

        if not self.client:
            raise ConnectionError("Device is not connected.")

        try:
            registers = self.client.read_holding_registers(address, quantity)
            if not registers:
                raise ValueError(f"Failed to read register '{name}' at address {address}.")
            return convert_registers_to_readable(registers, reg_info)
        except Exception as e:
            raise RuntimeError(f"Error reading register '{name}': {e}")

    async def read_raw_register(self, address, quantity):
        """
        Read raw registers directly by address and quantity.

        :param address: Starting address of the registers to read.
        :type address: int
        :param quantity: Number of registers to read.
        :type quantity: int
        :return: Raw register values.
        :rtype: list[int]
        :raises ConnectionError: If the device is not connected.
        :raises RuntimeError: If there is an error while reading the registers.
        """

        if not self.client:
            raise ConnectionError("Device is not connected.")

        try:
            registers = self.client.read_holding_registers(address, quantity)
            if not registers:
                raise ValueError(f"Failed to read registers at address {address}.")
            return registers
        except Exception as e:
            raise RuntimeError(f"Error reading raw registers at address {address}: {e}")

    async def read_all_registers(self):
        """
        Read all registers defined in the device's register mappings.

        :return: List of tuples with register name, value, and unit.
        :rtype: list[tuple[str, Any, str]]
        """

        results = []
        for key, reg_info in self.registers.items():
            address = reg_info['address']
            quantity = reg_info['quantity']
            unit = reg_info.get('unit', 'N/A')

            try:
                # Read the registers
                registers = self.client.read_holding_registers(address, quantity)
                if registers:
                    # Convert the registers to a readable value
                    value = convert_registers_to_readable(registers, reg_info)
                    results.append((key, value, unit))
                else:
                    results.append((key, None, unit))
            except Exception as e:
                print(f"Error processing register {key} at address {address}: {e}")
                results.append((key, f"Error: {e}", unit))
        return results

    def is_connected(self):
        """
        Check if the Modbus client is connected.

        :return: True if connected, False otherwise.
        :rtype: bool
        """

        return self.client is not None

    def get_device_id(self):
        """
        Get the device ID.

        :return: The device ID.
        :rtype: int
        """

        return self.device_id
