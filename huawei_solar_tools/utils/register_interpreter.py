"""
Register Conversion Utility

This module provides a utility function to convert raw Modbus register values into
human-readable formats based on metadata definitions.

Functions:
    - convert_registers_to_readable: Interprets raw Modbus register values using the provided
      register metadata.

Usage:
    Use `convert_registers_to_readable` to decode raw register data from a Modbus device into
    meaningful values like integers, strings, or bitfields.

Example:
    from register_interpreter import convert_registers_to_readable

    raw_registers = [0x1234, 0x5678]
    reg_info = {
        "type": "U32",
        "gain": 1,
        "address": 100
    }
    value = convert_registers_to_readable(raw_registers, reg_info)
    print(value)
"""

import struct

def convert_registers_to_readable(registers, reg_info):
    """
    Convert raw Modbus register values into a readable format based on register metadata.

    This function interprets raw Modbus data by applying metadata such as data type, gain,
    and other properties provided in the `reg_info` dictionary.

    Supported Data Types:
        - STR: Converts registers to a string (null-terminated).
        - U16, UINT16: Unsigned 16-bit integer.
        - I16, INT16: Signed 16-bit integer.
        - U32, UINT32: Unsigned 32-bit integer.
        - I32, INT32: Signed 32-bit integer.
        - U64: Unsigned 64-bit integer.
        - I64: Signed 64-bit integer.
        - Bitfield16: 16-bit bitfield.
        - Bitfield32: 32-bit bitfield.
        - MLD: Multi-length data (returns raw registers as-is).

    :param registers: List of raw Modbus register values.
    :type registers: list[int]
    :param reg_info: Dictionary containing register metadata (type, gain, etc.).
    :type reg_info: dict
    :return: Interpreted value based on the metadata.
    :rtype: str | int | float | list
    :raises ValueError: If the data type is unknown or if an error occurs during conversion.
    """

    try:
        if reg_info['type'] == 'STR':
            # Convert registers to a string
            return ''.join(chr((reg >> 8) & 0xFF) + chr(reg & 0xFF) for reg in registers).rstrip('\x00')
        elif reg_info['type'] in ('U16', 'UINT16'):
            return registers[0] / reg_info['gain']
        elif reg_info['type'] in ('I16', 'INT16'):
            return struct.unpack('h', struct.pack('H', registers[0]))[0] / reg_info['gain']
        elif reg_info['type'] in ('U32', 'UINT32', 'I32', 'U64', 'I64', 'INT32'):
            value = 0
            for reg in registers:
                value = (value << 16) | reg
            if reg_info['type'] == 'I32':
                value = struct.unpack('i', struct.pack('I', value & 0xFFFFFFFF))[0]
            elif reg_info['type'] in ('U32', 'UINT32'):
                value = value & 0xFFFFFFFF
            elif reg_info['type'] == 'U64':
                value = struct.unpack('>Q', struct.pack('>4H', *registers))[0]
            elif reg_info['type'] == 'I64':
                value = struct.unpack('>q', struct.pack('>4H', *registers))[0]
            return value / reg_info['gain']
        elif reg_info['type'] == 'Bitfield16':
            return registers[0]
        elif reg_info['type'] == 'Bitfield32':
            return (registers[0] << 16) | registers[1]
        elif reg_info['type'] == 'MLD':
            return registers
        else:
            raise ValueError(f"Unknown data type: {reg_info['type']}")
    except Exception as e:
        raise ValueError(f"Error processing registers at address {reg_info.get('address', 'unknown')}: {e}")
