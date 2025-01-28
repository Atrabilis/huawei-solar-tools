meter_registers = {
    "meter_status": {
        "address": 37100,
        "type": "UINT16",
        "unit": "N/A",
        "gain": 1,
        "quantity": 1,
        "description": "0: offline, 1: normal"
    },
    "grid_voltage_a_phase": {
        "address": 37101,
        "type": "INT32",
        "unit": "V",
        "gain": 10,
        "quantity": 2,
        "description": "Voltage of A phase"
    },
    "b_phase_voltage": {
        "address": 37103,
        "type": "INT32",
        "unit": "V",
        "gain": 10,
        "quantity": 2,
        "description": "Voltage of B phase"
    },
    "c_phase_voltage": {
        "address": 37105,
        "type": "INT32",
        "unit": "V",
        "gain": 10,
        "quantity": 2,
        "description": "Voltage of C phase"
    },
    "grid_current_a_phase": {
        "address": 37107,
        "type": "INT32",
        "unit": "A",
        "gain": 100,
        "quantity": 2,
        "description": "Current of A phase"
    },
    "b_phase_current": {
        "address": 37109,
        "type": "INT32",
        "unit": "A",
        "gain": 100,
        "quantity": 2,
        "description": "Current of B phase"
    },
    "c_phase_current": {
        "address": 37111,
        "type": "INT32",
        "unit": "A",
        "gain": 100,
        "quantity": 2,
        "description": "Current of C phase"
    },
    "active_power": {
        "address": 37113,
        "type": "INT32",
        "unit": "W",
        "gain": 1,
        "quantity": 2,
        "description": ">0: feed-in to the power grid, <0: supply from the power grid"
    },
    "reactive_power": {
        "address": 37115,
        "type": "INT32",
        "unit": "Var",
        "gain": 1,
        "quantity": 2,
        "description": ">0: feed-in to the power grid, <0: supply from the power grid"
    },
    "power_factor": {
        "address": 37117,
        "type": "INT16",
        "unit": "N/A",
        "gain": 1000,
        "quantity": 1,
        "description": "Power factor of the system"
    },
    "grid_frequency": {
        "address": 37118,
        "type": "INT16",
        "unit": "Hz",
        "gain": 100,
        "quantity": 1,
        "description": "Grid frequency"
    },
    "positive_active_electricity": {
        "address": 37119,
        "type": "INT32",
        "unit": "kWh",
        "gain": 100,
        "quantity": 2,
        "description": "Electricity fed by the inverter to the power grid"
    },
    "reverse_active_power": {
        "address": 37121,
        "type": "INT32",
        "unit": "kWh",
        "gain": 100,
        "quantity": 2,
        "description": "Power supplied to a distributed system from the power grid"
    },
    "accumulated_reactive_power": {
        "address": 37123,
        "type": "INT32",
        "unit": "kVarh",
        "gain": 100,
        "quantity": 2,
        "description": "Accumulated reactive power"
    },
    "meter_type": {
        "address": 37125,
        "type": "UINT16",
        "unit": "N/A",
        "gain": 1,
        "quantity": 1,
        "description": "0: single-phase, 1: three-phase"
    },
    "a_b_line_voltage": {
        "address": 37126,
        "type": "INT32",
        "unit": "V",
        "gain": 10,
        "quantity": 2,
        "description": "Voltage between A-B lines"
    },
    "b_c_line_voltage": {
        "address": 37128,
        "type": "INT32",
        "unit": "V",
        "gain": 10,
        "quantity": 2,
        "description": "Voltage between B-C lines"
    },
    "ca_line_voltage": {
        "address": 37130,
        "type": "INT32",
        "unit": "V",
        "gain": 10,
        "quantity": 2,
        "description": "Voltage between C-A lines"
    },
    "a_phase_active_power": {
        "address": 37132,
        "type": "INT32",
        "unit": "W",
        "gain": 1,
        "quantity": 2,
        "description": ">0: feed-in to the power grid, <0: supply from the power grid"
    },
    "b_phase_active_power": {
        "address": 37134,
        "type": "INT32",
        "unit": "W",
        "gain": 1,
        "quantity": 2,
        "description": ">0: feed-in to the power grid, <0: supply from the power grid"
    },
    "c_phase_active_power": {
        "address": 37136,
        "type": "INT32",
        "unit": "W",
        "gain": 1,
        "quantity": 2,
        "description": ">0: feed-in to the power grid, <0: supply from the power grid"
    },
    "meter_model_detection_result": {
        "address": 37138,
        "type": "UINT16",
        "unit": "N/A",
        "gain": 1,
        "quantity": 1,
        "description": "0: being identified, 1: model matches, 2: model mismatch"
    }
}
