"""
EMI Module

This module defines the `EMI` class, which extends the `Device` class to handle
specific functionalities of the EMI (Energy Management Interface) device as per
Huawei's technical documentation. The class uses Modbus communication to interact
with device registers.

Classes:
    - EMI: Represents the Huawei EMI device and provides access to its registers.

Usage:
    The `EMI` class can be instantiated with the IP address, port, and slave ID
    of the device. It inherits methods from the `Device` class for common operations
    like reading and writing registers.

Example:
    from huawei_solar_tools.devices.emi import EMI

    async def main():
        emi = EMI("192.168.1.101", 502, 1)
        await emi.connect()
        register_value = await emi.read_register_by_name("some_register_name")
        print(register_value)
        emi.disconnect()
"""


from huawei_solar_tools.devices.device import Device
from huawei_solar_tools.registers.emi_registers import emi_registers
class EMI(Device):
    """
    EMI Class

    Represents a Huawei Energy Management Interface (EMI) device. This class is designed
    to manage device-specific functionalities and interactions using Modbus communication.

    Inherits from:
        - Device: Base class for Modbus communication and register management.

    Attributes:
        - host (str): IP address of the device.
        - port (int): Port number for Modbus communication.
        - slave_id (int): Modbus slave ID of the device.
        - registers (dict): Dictionary of register mappings specific to the EMI device.
    """

    def __init__(self, host, port, slave_id):
        """
        Initialize the EMI device with the basic parameters for Modbus communication.

        :param host: IP address of the EMI device.
        :type host: str
        :param port: Port number for Modbus communication.
        :type port: int
        :param slave_id: Modbus slave ID of the EMI device.
        :type slave_id: int
        """

        super().__init__(host, port, slave_id, emi_registers)