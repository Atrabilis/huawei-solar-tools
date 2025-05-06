inverter_registers = {
    "model": {
        "read_write": "RO",
        "type": "STR",
        "unit": "N/A",
        "gain": 1,
        "address": 30000,
        "quantity": 15
    },
    "sn": {
        "read_write": "RO",
        "type": "STR",
        "unit": "N/A",
        "gain": 1,
        "address": 30015,
        "quantity": 10
    },
    "pn": {
        "read_write": "RO",
        "type": "STR",
        "unit": "N/A",
        "gain": 1,
        "address": 30025,
        "quantity": 10
    },
    "model_id": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 30070,
        "quantity": 1
    },
    "number_of_pv_strings": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 30071,
        "quantity": 1
    },
    "number_of_mpp_trackers": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 30072,
        "quantity": 1
    },
    "rated_power_pn": {
        "read_write": "RO",
        "type": "U32",
        "unit": "kW",
        "gain": 1000,
        "address": 30073,
        "quantity": 2
    },
    "maximum_active_power_pmax": {
        "read_write": "RO",
        "type": "U32",
        "unit": "kW",
        "gain": 1000,
        "address": 30075,
        "quantity": 2
    },
    "maximum_apparent_power_smax": {
        "read_write": "RO",
        "type": "U32",
        "unit": "kVA",
        "gain": 1000,
        "address": 30077,
        "quantity": 2
    },
    "maximum_reactive_power_qmax": {
        "read_write": "RO",
        "type": "I32",
        "unit": "kVar",
        "gain": 1000,
        "address": 30079,
        "quantity": 2
    },
    "maximum_reactive_power_qmax_absorbed": {
        "read_write": "RO",
        "type": "I32",
        "unit": "kVar",
        "gain": 1000,
        "address": 30081,
        "quantity": 2
    },
    "state_1": {
        "read_write": "RO",
        "type": "Bitfield16",
        "unit": "N/A",
        "gain": 1,
        "address": 32000,
        "quantity": 1
    },
    "state_2": {
        "read_write": "RO",
        "type": "Bitfield16",
        "unit": "N/A",
        "gain": 1,
        "address": 32002,
        "quantity": 1
    },
    "state_3": {
        "read_write": "RO",
        "type": "Bitfield32",
        "unit": "N/A",
        "gain": 1,
        "address": 32003,
        "quantity": 2
    },
    "alarm_1": {
        "read_write": "RO",
        "type": "Bitfield16",
        "unit": "N/A",
        "gain": 1,
        "address": 32008,
        "quantity": 1
    },
    "alarm_2": {
        "read_write": "RO",
        "type": "Bitfield16",
        "unit": "N/A",
        "gain": 1,
        "address": 32009,
        "quantity": 1
    },
    "alarm_3": {
        "read_write": "RO",
        "type": "Bitfield16",
        "unit": "N/A",
        "gain": 1,
        "address": 32010,
        "quantity": 1
    },
    "pv1_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32016,
        "quantity": 1
    },
    "pv1_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32017,
        "quantity": 1
    },
    "pv2_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32018,
        "quantity": 1
    },
    "pv2_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32019,
        "quantity": 1
    },
    "pv3_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32020,
        "quantity": 1
    },
    "pv3_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32021,
        "quantity": 1
    },
    "pv4_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32022,
        "quantity": 1
    },
    "pv4_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32023,
        "quantity": 1
    },
    "pv5_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32024,
        "quantity": 1
    },
    "pv5_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32025,
        "quantity": 1
    },
    "pv6_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32026,
        "quantity": 1
    },
    "pv6_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32027,
        "quantity": 1
    },
    "pv7_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32028,
        "quantity": 1
    },
    "pv7_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32029,
        "quantity": 1
    },
    "pv8_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32030,
        "quantity": 1
    },
    "pv8_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32031,
        "quantity": 1
    },
    "pv9_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32032,
        "quantity": 1
    },
    "pv9_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32033,
        "quantity": 1
    },
    "pv10_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32034,
        "quantity": 1
    },
    "pv10_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32035,
        "quantity": 1
    },
    "pv11_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32036,
        "quantity": 1
    },
    "pv11_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32037,
        "quantity": 1
    },
    "pv12_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32038,
        "quantity": 1
    },
    "pv12_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32039,
        "quantity": 1
    },
    "pv13_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32040,
        "quantity": 1
    },
    "pv13_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32041,
        "quantity": 1
    },
    "pv14_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32042,
        "quantity": 1
    },
    "pv14_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32043,
        "quantity": 1
    },
    "pv15_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32044,
        "quantity": 1
    },
    "pv15_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32045,
        "quantity": 1
    },
    "pv16_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32046,
        "quantity": 1
    },
    "pv16_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32047,
        "quantity": 1
    },
    "pv17_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32048,
        "quantity": 1
    },
    "pv17_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32049,
        "quantity": 1
    },
    "pv18_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32050,
        "quantity": 1
    },
    "pv18_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32051,
        "quantity": 1
    },
    "pv19_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32052,
        "quantity": 1
    },
    "pv19_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32053,
        "quantity": 1
    },
    "pv20_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32054,
        "quantity": 1
    },
    "pv20_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32055,
        "quantity": 1
    },
    "pv21_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32056,
        "quantity": 1
    },
    "pv21_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32057,
        "quantity": 1
    },
    "pv22_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32058,
        "quantity": 1
    },
    "pv22_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32059,
        "quantity": 1
    },
    "pv23_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32060,
        "quantity": 1
    },
    "pv23_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32061,
        "quantity": 1
    },
    "pv24_voltage": {
        "read_write": "RO",
        "type": "I16",
        "unit": "V",
        "gain": 10,
        "address": 32062,
        "quantity": 1
    },
    "pv24_current": {
        "read_write": "RO",
        "type": "I16",
        "unit": "A",
        "gain": 100,
        "address": 32063,
        "quantity": 1
    },
    "input_power": {
        "read_write": "RO",
        "type": "I32",
        "unit": "kW",
        "gain": 1000,
        "address": 32064,
        "quantity": 2
    },
    "power_grid_voltage_line_a_b": {
        "read_write": "RO",
        "type": "U16",
        "unit": "V",
        "gain": 10,
        "address": 32066,
        "quantity": 1
    },
    "line_voltage_between_b_c": {
        "read_write": "RO",
        "type": "U16",
        "unit": "V",
        "gain": 10,
        "address": 32067,
        "quantity": 1
    },
    "line_voltage_between_c_a": {
        "read_write": "RO",
        "type": "U16",
        "unit": "V",
        "gain": 10,
        "address": 32068,
        "quantity": 1
    },
    "phase_a_voltage": {
        "read_write": "RO",
        "type": "U16",
        "unit": "V",
        "gain": 10,
        "address": 32069,
        "quantity": 1
    },
    "phase_b_voltage": {
        "read_write": "RO",
        "type": "U16",
        "unit": "V",
        "gain": 10,
        "address": 32070,
        "quantity": 1
    },
    "phase_c_voltage": {
        "read_write": "RO",
        "type": "U16",
        "unit": "V",
        "gain": 10,
        "address": 32071,
        "quantity": 1
    },
    "power_grid_current_phase_a": {
        "read_write": "RO",
        "type": "I32",
        "unit": "A",
        "gain": 1000,
        "address": 32072,
        "quantity": 2
    },
    "phase_b_current": {
        "read_write": "RO",
        "type": "I32",
        "unit": "A",
        "gain": 1000,
        "address": 32074,
        "quantity": 2
    },
    "phase_c_current": {
        "read_write": "RO",
        "type": "I32",
        "unit": "A",
        "gain": 1000,
        "address": 32076,
        "quantity": 2
    },
    "peak_active_power_current_day": {
        "read_write": "RO",
        "type": "I32",
        "unit": "kW",
        "gain": 1000,
        "address": 32078,
        "quantity": 2
    },
    "active_power": {
        "read_write": "RO",
        "type": "I32",
        "unit": "kW",
        "gain": 1000,
        "address": 32080,
        "quantity": 2
    },
    "reactive_power": {
        "read_write": "RO",
        "type": "I32",
        "unit": "kVar",
        "gain": 1000,
        "address": 32082,
        "quantity": 2
    },
    "power_factor": {
        "read_write": "RO",
        "type": "I16",
        "unit": "N/A",
        "gain": 1000,
        "address": 32084,
        "quantity": 1
    },
    "grid_frequency": {
        "read_write": "RO",
        "type": "U16",
        "unit": "Hz",
        "gain": 100,
        "address": 32085,
        "quantity": 1
    },
    "efficiency": {
        "read_write": "RO",
        "type": "U16",
        "unit": "%",
        "gain": 100,
        "address": 32086,
        "quantity": 1
    },
    "internal_temperature": {
        "read_write": "RO",
        "type": "I16",
        "unit": "°C",
        "gain": 10,
        "address": 32087,
        "quantity": 1
    },
    "insulation_resistance": {
        "read_write": "RO",
        "type": "U16",
        "unit": "MΩ",
        "gain": 1000,
        "address": 32088,
        "quantity": 1
    },
    "device_status": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 32089,
        "quantity": 1
    },
    "fault_code": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 32090,
        "quantity": 1
    },
    "startup_time": {
        "read_write": "RO",
        "type": "U32",
        "unit": "N/A",
        "gain": 1,
        "address": 32091,
        "quantity": 2
    },
    "shutdown_time": {
        "read_write": "RO",
        "type": "U32",
        "unit": "N/A",
        "gain": 1,
        "address": 32093,
        "quantity": 2
    },
    "accumulated_energy_yield": {
        "read_write": "RO",
        "type": "U32",
        "unit": "kWh",
        "gain": 100,
        "address": 32106,
        "quantity": 2
    },
    "daily_energy_yield": {
        "read_write": "RO",
        "type": "U32",
        "unit": "kWh",
        "gain": 100,
        "address": 32114,
        "quantity": 2
    },
    "active_adjustment_mode": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 35300,
        "quantity": 1
    },
    "active_adjustment_value": {
        "read_write": "RO",
        "type": "U32",
        "unit": "N/A",
        "gain": "*",
        "address": 35302,
        "quantity": 2
    },
    "fault_code": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 32090,
        "quantity": 1
    },
    "startup_time": {
        "read_write": "RO",
        "type": "U32",
        "unit": "N/A",
        "gain": 1,
        "address": 32091,
        "quantity": 2
    },
    "shutdown_time": {
        "read_write": "RO",
        "type": "U32",
        "unit": "N/A",
        "gain": 1,
        "address": 32093,
        "quantity": 2
    },
    "accumulated_energy_yield": {
        "read_write": "RO",
        "type": "U32",
        "unit": "kWh",
        "gain": 100,
        "address": 32106,
        "quantity": 2
    },
    "daily_energy_yield": {
        "read_write": "RO",
        "type": "U32",
        "unit": "kWh",
        "gain": 100,
        "address": 32114,
        "quantity": 2
    },
    "active_adjustment_mode": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 35300,
        "quantity": 1
    },
    "active_adjustment_value": {
        "read_write": "RO",
        "type": "U32",
        "unit": "N/A",
        "gain": "*",
        "address": 35302,
        "quantity": 2
    },
    "active_adjustment_command": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 35303,
        "quantity": 1
    },
    "reactive_adjustment_mode": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 35304,
        "quantity": 1
    },
    "reactive_adjustment_value": {
        "read_write": "RO",
        "type": "U32",
        "unit": "N/A",
        "gain": "*",
        "address": 35305,
        "quantity": 2
    },
    "reactive_adjustment_command": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 35307,
        "quantity": 1
    },
    "power_meter_collection_active_power": {
        "read_write": "RO",
        "type": "I32",
        "unit": "W",
        "gain": 1,
        "address": 37113,
        "quantity": 2
    },
    "optimizer_total_number": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 37200,
        "quantity": 1
    },
    "optimizer_online_number": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 37201,
        "quantity": 1
    },
    "optimizer_feature_data": {
        "read_write": "RO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 37202,
        "quantity": 1
    },
    "system_time": {
        "read_write": "RW",
        "type": "U32",
        "unit": "N/A",
        "gain": 1,
        "address": 40000,
        "quantity": 2
    },
    "power_grid_scheduling_qu_characteristic_curve_mode": {
        "read_write": "RW",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 40037,
        "quantity": 1
    },
    "power_grid_scheduling_qu_dispatch_trigger_power_percentage": {
        "read_write": "RW",
        "type": "U16",
        "unit": "%",
        "gain": 1,
        "address": 40038,
        "quantity": 1
    },
    "power_grid_scheduling_fixed_active_power_derated": {
        "read_write": "RW",
        "type": "U16",
        "unit": "kW",
        "gain": 10,
        "address": 40120,
        "quantity": 1
    },
    "power_grid_scheduling_reactive_power_compensation_pf": {
        "read_write": "RW",
        "type": "I16",
        "unit": "N/A",
        "gain": 1000,
        "address": 40122,
        "quantity": 1
    },
    "power_grid_scheduling_reactive_power_compensation_qs": {
        "read_write": "RW",
        "type": "I16",
        "unit": "N/A",
        "gain": 1000,
        "address": 40123,
        "quantity": 1
    },
    "power_grid_scheduling_active_power_percentage_derating": {
        "read_write": "RW",
        "type": "U16",
        "unit": "%",
        "gain": 10,
        "address": 40123,
        "quantity": 1
    },
    "power_grid_scheduling_fixed_active_power_derated_w": {
        "read_write": "RW",
        "type": "U32",
        "unit": "W",
        "gain": 1,
        "address": 40126,
        "quantity": 2
    },
    "power_grid_scheduling_reactive_power_compensation_night_kvar": {
        "read_write": "RW",
        "type": "I32",
        "unit": "kVar",
        "gain": 1000,
        "address": 40129,
        "quantity": 2
    },
    "power_grid_scheduling_cos_phi_p_pn_characteristic_curve": {
        "read_write": "RW",
        "type": "MLD",
        "unit": "N/A",
        "gain": 1,
        "address": 40133,
        "quantity": 21
    },
    "power_grid_scheduling_qu_characteristic_curve": {
        "read_write": "RW",
        "type": "MLD",
        "unit": "N/A",
        "gain": 1,
        "address": 40154,
        "quantity": 21
    },
    "power_grid_scheduling_pf_u_characteristic_curve": {
        "read_write": "RW",
        "type": "MLD",
        "unit": "N/A",
        "gain": 1,
        "address": 40175,
        "quantity": 21
    },
    "power_grid_scheduling_reactive_power_adjustment_time": {
        "read_write": "RW",
        "type": "U16",
        "unit": "s",
        "gain": 1,
        "address": 40196,
        "quantity": 1
    },
    "power_grid_scheduling_qu_power_percentage_to_exit_scheduling": {
        "read_write": "RW",
        "type": "U16",
        "unit": "%",
        "gain": 1,
        "address": 40198,
        "quantity": 1
    },
    "startup": {
        "read_write": "WO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 40200,
        "quantity": 1
    },
    "shutdown": {
        "read_write": "WO",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 40201,
        "quantity": 1
    },
    "grid_code": {
        "read_write": "RW",
        "type": "U16",
        "unit": "N/A",
        "gain": 1,
        "address": 42000,
        "quantity": 1
    },
    "power_grid_scheduling_reactive_power_change_gradient": {
        "read_write": "RW",
        "type": "U32",
        "unit": "%/s",
        "gain": 1000,
        "address": 42015,
        "quantity": 2
    },
    "power_grid_scheduling_active_power_change_gradient": {
        "read_write": "RW",
        "type": "U32",
        "unit": "%/s",
        "gain": 1000,
        "address": 42017,
        "quantity": 2
    },
    "power_grid_scheduling_schedule_instruction_valid_duration": {
        "read_write": "RW",
        "type": "U32",
        "unit": "s",
        "gain": 1,
        "address": 42019,
        "quantity": 2
    },
    "time_zone": {
        "read_write": "RW",
        "type": "I16",
        "unit": "min",
        "gain": 1,
        "address": 43006,
        "quantity": 1
    }
}
