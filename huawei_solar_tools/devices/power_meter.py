"""
PowerMeter Module

This module defines the `PowerMeter` class, which extends the `Device` class to manage
Huawei power meter-specific functionalities. It uses Modbus communication to interact
with the power meter's registers, enabling data collection and operational monitoring.

Classes:
    - PowerMeter: Represents a Huawei power meter and provides access to its registers.

Usage:
    The `PowerMeter` class can be instantiated using the IP address, port, and device ID
    of the power meter. It inherits methods from the `Device` class for operations such as
    reading and writing registers.

Example:
    from huawei_solar_tools.devices.power_meter import PowerMeter

    async def main():
        power_meter = PowerMeter("192.168.1.160", 502, 1)
        await power_meter.connect()
        active_power = await power_meter.read_register_by_name("active_power")
        print(f"Active Power: {active_power}")
        power_meter.disconnect()
"""


from huawei_solar_tools.devices.device import Device
from huawei_solar_tools.registers.power_meter_registers import power_meter_registers
class PowerMeter(Device):
    """
    PowerMeter Class

    Represents a Huawei power meter device. Designed to manage power meter-specific
    functionalities using Modbus communication and predefined register mappings.

    Inherits from:
        - Device: Base class for Modbus communication and register management.

    Attributes:
        - host (str): IP address of the power meter.
        - port (int): Port number for Modbus communication.
        - slave_id (int): Modbus slave ID of the power meter.
        - registers (dict): Dictionary of register mappings specific to the power meter.
    """

    def __init__(self, host, port, slave_id):
        """
        Initialize the PowerMeter device with the basic parameters for Modbus communication.

        :param host: IP address of the power meter device.
        :type host: str
        :param port: Port number for Modbus communication.
        :type port: int
        :param slave_id: Modbus slave ID of the power meter device.
        :type slave_id: int
        """

        super().__init__(host, port, slave_id, power_meter_registers)