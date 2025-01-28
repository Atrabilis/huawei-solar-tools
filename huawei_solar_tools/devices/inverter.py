"""
Inverter Module

This module defines the `Inverter` class, which extends the `Device` class to manage
specific operations of Huawei solar inverters. The class includes methods for interpreting
states, alarms, characteristic curves, and grid codes, as well as retrieving operational
timestamps.

Classes:
    - Inverter: Represents a Huawei inverter and provides functionality for state,
      alarm interpretation, and more.

Usage:
    The `Inverter` class can be instantiated using the IP address, port, and device ID of the
    inverter. It relies on Modbus communication for accessing and processing data.

Example:
    from huawei_solar_tools.devices.inverter import Inverter

    async def main():
        inverter = Inverter("192.168.1.200", 502, 1)
        await inverter.connect()
        states = await inverter.interpret_states()
        print(states)
        await inverter.disconnect()
"""

from datetime import datetime, timezone
from huawei_solar_tools.devices.device import Device
from huawei_solar_tools.registers.inverter_registers import inverter_registers
from huawei_solar_tools.registers.inverter_register_names import *  # Import constants for linting support
from huawei_solar_tools.registers.grid_codes import grid_codes  # Import the grid_codes dictionary


class Inverter(Device):
    """
    Inverter Class

    Represents a Huawei solar inverter. Provides methods to interpret inverter-specific states,
    alarms, characteristic curves, and grid codes, along with retrieving operational timestamps.

    Inherits from:
        - Device: Base class for Modbus communication and register management.

    Attributes:
        - host (str): IP address of the inverter.
        - port (int): Port number for Modbus communication.
        - device_id (int): Modbus slave ID of the inverter.
        - registers (dict): Dictionary of register mappings specific to the inverter.
    """
    def __init__(self, host, port, device_id):
        """
        Initialize the Inverter with its specific register mappings.

        :param host: IP address of the Modbus server.
        :param port: Port of the Modbus server.
        :param device_id: Modbus unit ID of the inverter.
        """
        super().__init__(host, port, device_id, inverter_registers)

    async def interpret_states(self):
        """
        Interpret the state registers for the inverter.

        :return: Dictionary containing the interpreted states for state_1, state_2, and state_3.
        :rtype: dict
        :raises RuntimeError: If there is an error while interpreting states.
        """

        try:
            state_1 = await self.read_register_by_name(STATE_1)
            state_2 = await self.read_register_by_name(STATE_2)
            state_3 = await self.read_register_by_name(STATE_3)
            return {
                "state_1": self._interpret_state_1(state_1),
                "state_2": self._interpret_state_2(state_2),
                "state_3": self._interpret_state_3(state_3),
            }
        except Exception as e:
            raise RuntimeError(f"Error interpreting states: {e}")

    async def interpret_alarms(self):
        """
        Interpret the alarm registers for the inverter.

        :return: Dictionary containing the interpreted alarms from alarm_1, alarm_2, and alarm_3.
        :rtype: dict
        :raises RuntimeError: If there is an error while interpreting alarms.
        """

        try:
            alarm_1 = await self.read_register_by_name(ALARM_1)
            alarm_2 = await self.read_register_by_name(ALARM_2)
            alarm_3 = await self.read_register_by_name(ALARM_3)
            return {
                "General Alarms": self._interpret_alarm_1(alarm_1),
                "Advanced Alarms": self._interpret_alarm_2(alarm_2),
                "Device Faults": self._interpret_alarm_3(alarm_3),
            }
        except Exception as e:
            raise RuntimeError(f"Error interpreting alarms: {e}")

    async def interpret_cos_phi_p_pn_curve(self):
        """
        Interpret the cosφ-P/Pn characteristic curve by reading and processing the corresponding registers.

        :return: List of dictionaries containing "P/Pn" and "cosφ" values.
        :rtype: list[dict[str, float]]
        :raises RuntimeError: If there is an error while interpreting the curve.
        """

        try:
            raw_data = await self.read_register_by_name("power_grid_scheduling_cos_phi_p_pn_characteristic_curve")
            return self._process_cos_phi_p_pn_curve(raw_data)
        except Exception as e:
            raise RuntimeError(f"Error interpreting cosφ-P/Pn curve: {e}")

    async def interpret_qu_curve(self):
        """
        Interpret the Q-U characteristic curve by reading the corresponding registers.

        :return: List of dictionaries with "U" and "Q" values.
        """
        try:
            raw_data = await self.read_register_by_name("power_grid_scheduling_qu_characteristic_curve")
            return self._process_qu_curve(raw_data)
        except Exception as e:
            raise RuntimeError(f"Error interpreting Q-U curve: {e}")

    async def interpret_pf_u_curve(self):
        """
        Interpret the PF-U characteristic curve by reading the corresponding registers.

        :return: List of dictionaries with "U" and "PF" values.
        """
        try:
            raw_data = await self.read_register_by_name("power_grid_scheduling_pf_u_characteristic_curve")
            return self._process_pf_u_curve(raw_data)
        except Exception as e:
            raise RuntimeError(f"Error interpreting PF-U curve: {e}")


    def _process_cos_phi_p_pn_curve(self, raw_data):
        """
        Process raw data for the cosφ-P/Pn curve.
        """
        num_points = raw_data[0]  # Number of points
        if not (2 <= num_points <= 10):
            raise ValueError(f"Invalid number of points: {num_points}")

        curve = []
        for i in range(num_points):
            p_pn = raw_data[1 + i * 2] / 10  # P/Pn with gain 10
            cos_phi = raw_data[2 + i * 2] / 1000  # cosφ with gain 1000
            curve.append({"P/Pn": p_pn, "cosφ": cos_phi})
        return curve

    def _process_qu_curve(self, raw_data):
        """
        Process raw data for the Q-U curve.
        """
        num_points = raw_data[0]  # Number of points
        if not (2 <= num_points <= 10):
            raise ValueError(f"Invalid number of points: {num_points}")

        curve = []
        for i in range(num_points):
            u = raw_data[1 + i * 2] / 10  # U with gain 10
            q = raw_data[2 + i * 2] / 1000  # Q with gain 1000
            curve.append({"U": u, "Q": q})
        return curve

    def _process_pf_u_curve(self, raw_data):
        """
        Process raw data for the PF-U curve.
        """
        if not raw_data or len(raw_data) < 1:
            raise ValueError("Raw data is empty or invalid.")

        num_points = raw_data[0]  # Number of points
        if num_points == 0:
            print("Warning: No points available in PF-U curve data.")
            return []  # Gracefully handle zero points

        if not (2 <= num_points <= 10):
            raise ValueError(f"Invalid number of points: {num_points}")

        curve = []
        for i in range(num_points):
            u = raw_data[1 + i * 2] / 10  # U with gain 10
            pf = raw_data[2 + i * 2] / 1000  # PF with gain 1000
            curve.append({"U": u, "PF": pf})
        return curve

    
    def _interpret_state_1(self, raw_value):
        """
        Internal helper to interpret state_1 bitfield.
        """
        state_map = {
            0: "Standby",
            1: "Grid-connected",
            2: "Grid-connected normally",
            3: "Grid-connected with derating",
            4: "Stopped due to faults",
            5: "Shutdown",
        }
        return [desc for bit, desc in state_map.items() if raw_value & (1 << bit)]

    def _interpret_state_2(self, raw_value):
        """
        Internal helper to interpret state_2 bitfield.
        """
        state_map = {
            0: "Locked" if raw_value & (1 << 0) == 0 else "Unlocked",
            1: "PV disconnected" if raw_value & (1 << 1) == 0 else "PV connected",
        }
        return [desc for desc in state_map.values()]

    def _interpret_state_3(self, raw_value):
        """
        Internal helper to interpret state_3 bitfield.
        """
        state_map = {
            0: "On-grid" if raw_value & (1 << 0) == 0 else "Off-grid",
            1: "Off-grid switch: Disabled" if raw_value & (1 << 1) == 0 else "Off-grid switch: Enabled",
        }
        return [desc for desc in state_map.values()]

    def _interpret_alarm_1(self, raw_value):
        """
        Internal helper to interpret general alarms from alarm_1.
        """
        alarm_map = {
            0: "High string input voltage",
            1: "DC arc fault",
            2: "String reverse connection",
            3: "String current backfeed",
            4: "Abnormal string power",
            5: "AFCI self-check fail",
            6: "Phase wire short-circuited to PE",
            7: "Grid loss",
        }
        return [desc for bit, desc in alarm_map.items() if raw_value & (1 << bit)]

    def _interpret_alarm_2(self, raw_value):
        """
        Internal helper to interpret advanced alarms from alarm_2.
        """
        alarm_map = {
            0: "Abnormal residual current",
            1: "Ground fault",
            2: "Low insulation resistance",
            3: "Overtemperature",
            4: "Device fault",
            5: "Upgrade failed or version mismatch",
            6: "License expired",
            7: "Faulty monitoring unit",
        }
        return [desc for bit, desc in alarm_map.items() if raw_value & (1 << bit)]

    def _interpret_alarm_3(self, raw_value):
        """
        Internal helper to interpret device faults from alarm_3.
        """
        alarm_map = {
            0: "Optimizer fault",
            1: "Built-in PID operation abnormal",
            2: "High input string voltage to ground",
            3: "External fan abnormal",
            4: "Battery reverse connection",
            5: "On-grid/off-grid controller abnormal",
            6: "PV string loss",
            7: "Internal fan abnormal",
            8: "DC protection unit abnormal",
            9: "EL unit abnormal",
        }
        return [desc for bit, desc in alarm_map.items() if raw_value & (1 << bit)]

    async def get_startup_time(self, iso=False):
        """
        Fetch and convert the inverter's startup time to a UTC datetime object or ISO 8601 format.

        :param iso: If True, return the datetime in ISO 8601 format.
        :type iso: bool
        :return: Startup time as a datetime object or ISO string, or None if unavailable.
        :rtype: datetime | str | None
        :raises RuntimeError: If there is an error while retrieving the startup time.
        """

        raw_time = await self.read_register_by_name("startup_time")
        if raw_time:
            dt = datetime.fromtimestamp(raw_time, tz=timezone.utc)
            return dt.isoformat() if iso else dt
        return None

    async def get_shutdown_time(self, iso=False):
        """
        Fetch and convert the shutdown time to a UTC datetime object or ISO format.

        :param iso: If True, return the datetime in ISO 8601 format.
        :return: Shutdown time as a datetime object or ISO string, or None if uninitialized.
        """
        raw_time = await self.read_register_by_name("shutdown_time")
        if raw_time:
            # Handle max UNIX timestamp (uninitialized)
            if raw_time == 2_147_483_647:
                return None
            dt = datetime.fromtimestamp(raw_time, tz=timezone.utc)
            return dt.isoformat() if iso else dt
        return None

    async def interpret_grid_code(self):
        """
        Interpret the grid code from the inverter's register value.

        :return: Dictionary with the grid code and its description, or None if the code is invalid.
        :rtype: dict[str, Any] | None
        :raises RuntimeError: If there is an error while interpreting the grid code.
        """

        try:
            # Read the grid code value from the relevant register
            grid_code_value = await self.read_register_by_name("grid_code")
            if grid_code_value is not None:
                # Lookup the grid code in the grid_codes dictionary
                grid_code_info = grid_codes.get(grid_code_value)
                if grid_code_info:
                    return {"code": grid_code_value, "description": grid_code_info}
                else:
                    return {"code": grid_code_value, "description": "Unknown grid code"}
            else:
                return None
        except Exception as e:
            raise RuntimeError(f"Error interpreting grid code: {e}")