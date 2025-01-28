"""
Meter Module

This module defines the `Meter` class, which extends the `Device` class to manage
Huawei meter-specific functionalities. The class uses Modbus communication to interact
with the meter's registers, enabling data collection and operational insights.

Classes:
    - Meter: Represents a Huawei meter and provides methods to access its functionalities.

Usage:
    The `Meter` class can be instantiated using the IP address, port, and device ID
    of the meter. It inherits methods from the `Device` class for operations such as
    reading and writing registers.

Example:
    from huawei_solar_tools.devices.meter import Meter

    async def main():
        meter = Meter("192.168.1.150", 502, 1)
        await meter.connect()
        register_value = await meter.read_register_by_name("active_power")
        print(register_value)
        meter.disconnect()
"""


from huawei_solar_tools.devices.device import Device
from huawei_solar_tools.registers.meter_registers import meter_registers
class Meter(Device):
    """
    Meter Class

    Represents a Huawei meter device. Designed to manage meter-specific functionalities
    using Modbus communication and pre-defined register mappings.

    Inherits from:
        - Device: Base class for Modbus communication and register management.

    Attributes:
        - host (str): IP address of the meter.
        - port (int): Port number for Modbus communication.
        - slave_id (int): Modbus slave ID of the meter.
        - registers (dict): Dictionary of register mappings specific to the meter.
    """

    def __init__(self, host, port, slave_id):
        """
        Initialize the Meter device with the basic parameters for Modbus communication.

        :param host: IP address of the meter device.
        :type host: str
        :param port: Port number for Modbus communication.
        :type port: int
        :param slave_id: Modbus slave ID of the meter device.
        :type slave_id: int
        """

        super().__init__(host, port, slave_id, meter_registers)