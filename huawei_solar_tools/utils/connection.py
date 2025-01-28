"""
Modbus TCP Client Creation Module

This module provides a utility function to create and manage Modbus TCP client connections.

Functions:
    - create_modbus_tcp_client: Asynchronously creates and returns a Modbus TCP client instance.

Usage:
    The `create_modbus_tcp_client` function establishes a connection to a Modbus TCP server and returns a client instance
    that can be used for Modbus communication.

Example:
    from my_modbus_module import create_modbus_tcp_client

    async def main():
        client = await create_modbus_tcp_client("192.168.1.100", 502, 1)
        if client:
            print("Connection successful!")
        else:
            print("Connection failed.")
"""

from pyModbusTCP.client import ModbusClient

async def create_modbus_tcp_client(host, port, unit_id, timeout=10):
    """
    Create and return a Modbus TCP client.

    This function establishes a connection to a Modbus TCP server using the specified
    parameters and returns an instance of the `ModbusClient` for further communication.

    :param host: IP address of the Modbus server.
    :type host: str
    :param port: Port number of the Modbus server.
    :type port: int
    :param unit_id: Modbus device unit ID.
    :type unit_id: int
    :param timeout: Connection timeout in seconds (default is 10).
    :type timeout: int
    :return: An instance of `ModbusClient` if the connection is successful, or None otherwise.
    :rtype: ModbusClient | None
    """

    client = ModbusClient(host=host, port=port, auto_open=True, unit_id=unit_id, timeout=timeout)
    if client.open():
        print(f"Connected to Modbus device {unit_id} at {host}:{port}")
        return client
    else:
        print(f"Failed to connect to Modbus device {unit_id} at {host}:{port}")
        return None

