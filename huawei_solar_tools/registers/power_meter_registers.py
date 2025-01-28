power_meter_registers = {
    "phase_a_voltage": {
        "address": 32260,
        "type": "U32",
        "unit": "V",
        "gain": 100,
        "quantity": 2,
        "description": "Voltage of Phase A"
    },
    "phase_b_voltage": {
        "address": 32262,
        "type": "U32",
        "unit": "V",
        "gain": 100,
        "quantity": 2,
        "description": "Voltage of Phase B"
    },
    "phase_c_voltage": {
        "address": 32264,
        "type": "U32",
        "unit": "V",
        "gain": 100,
        "quantity": 2,
        "description": "Voltage of Phase C"
    },
    "a_b_line_voltage": {
        "address": 32266,
        "type": "U32",
        "unit": "V",
        "gain": 100,
        "quantity": 2,
        "description": "Voltage between A-B lines"
    },
    "b_c_line_voltage": {
        "address": 32268,
        "type": "U32",
        "unit": "V",
        "gain": 100,
        "quantity": 2,
        "description": "Voltage between B-C lines"
    },
    "c_a_line_voltage": {
        "address": 32270,
        "type": "U32",
        "unit": "V",
        "gain": 100,
        "quantity": 2,
        "description": "Voltage between C-A lines"
    },
    "phase_a_current": {
        "address": 32272,
        "type": "I32",
        "unit": "A",
        "gain": 10,
        "quantity": 2,
        "description": "Current of Phase A"
    },
    "phase_b_current": {
        "address": 32274,
        "type": "I32",
        "unit": "A",
        "gain": 10,
        "quantity": 2,
        "description": "Current of Phase B"
    },
    "phase_c_current": {
        "address": 32276,
        "type": "I32",
        "unit": "A",
        "gain": 10,
        "quantity": 2,
        "description": "Current of Phase C"
    },
    "active_power": {
        "address": 32278,
        "type": "I32",
        "unit": "kW",
        "gain": 1000,
        "quantity": 2,
        "description": "Total active power"
    },
    "reactive_power": {
        "address": 32280,
        "type": "I32",
        "unit": "kVar",
        "gain": 1000,
        "quantity": 2,
        "description": "Total reactive power"
    },
    "active_electricity_reserved": {
        "address": 32282,
        "type": "I32",
        "unit": "kWh",
        "gain": 10,
        "quantity": 2,
        "description": "Active electricity (reserved)"
    },
    "power_factor": {
        "address": 32284,
        "type": "I16",
        "unit": "N/A",
        "gain": 1000,
        "quantity": 1,
        "description": "Power factor"
    },
    "reactive_electricity_reserved": {
        "address": 32285,
        "type": "I32",
        "unit": "kVarh",
        "gain": 10,
        "quantity": 2,
        "description": "Reactive electricity (reserved)"
    },
    "apparent_power": {
        "address": 32287,
        "type": "I32",
        "unit": "kVA",
        "gain": 1000,
        "quantity": 2,
        "description": "Total apparent power"
    },
    "positive_active_electricity_reserved": {
        "address": 32289,
        "type": "I32",
        "unit": "kWh",
        "gain": 100,
        "quantity": 2,
        "description": "Positive active electricity (reserved)"
    },
    "positive_reactive_electricity_reserved": {
        "address": 32291,
        "type": "I32",
        "unit": "kVarh",
        "gain": 100,
        "quantity": 2,
        "description": "Positive reactive electricity (reserved)"
    },
    "electricity_in_positive_active_price_segment_1": {
        "address": 32299,
        "type": "I32",
        "unit": "kWh",
        "gain": 100,
        "quantity": 2,
        "description": "Electricity in positive active electricity price segment 1"
    },
    "electricity_in_positive_active_price_segment_2": {
        "address": 32301,
        "type": "I32",
        "unit": "kWh",
        "gain": 100,
        "quantity": 2,
        "description": "Electricity in positive active electricity price segment 2"
    },
    "electricity_in_positive_active_price_segment_3": {
        "address": 32303,
        "type": "I32",
        "unit": "kWh",
        "gain": 100,
        "quantity": 2,
        "description": "Electricity in positive active electricity price segment 3"
    },
    "electricity_in_positive_active_price_segment_4": {
        "address": 32305,
        "type": "I32",
        "unit": "kWh",
        "gain": 100,
        "quantity": 2,
        "description": "Electricity in positive active electricity price segment 4"
    },
    "phase_a_active_power": {
        "address": 32335,
        "type": "I32",
        "unit": "kW",
        "gain": 1000,
        "quantity": 2,
        "description": "Phase A active power"
    },
    "phase_b_active_power": {
        "address": 32337,
        "type": "I32",
        "unit": "kW",
        "gain": 1000,
        "quantity": 2,
        "description": "Phase B active power"
    },
    "phase_c_active_power": {
        "address": 32339,
        "type": "I32",
        "unit": "kW",
        "gain": 1000,
        "quantity": 2,
        "description": "Phase C active power"
    },
    "total_active_electricity": {
        "address": 32341,
        "type": "I64",
        "unit": "kWh",
        "gain": 100,
        "quantity": 4,
        "description": "Total active electricity"
    },
    "total_reactive_electricity": {
        "address": 32345,
        "type": "I64",
        "unit": "kVarh",
        "gain": 100,
        "quantity": 4,
        "description": "Total reactive electricity"
    },
    "negative_active_electricity": {
        "address": 32349,
        "type": "I64",
        "unit": "kWh",
        "gain": 100,
        "quantity": 4,
        "description": "Negative active electricity"
    },
    "negative_reactive_electricity": {
        "address": 32353,
        "type": "I64",
        "unit": "kVarh",
        "gain": 100,
        "quantity": 4,
        "description": "Negative reactive electricity"
    },
    "positive_active_electricity": {
        "address": 32357,
        "type": "I64",
        "unit": "kWh",
        "gain": 100,
        "quantity": 4,
        "description": "Positive active electricity"
    },
    "positive_reactive_electricity": {
        "address": 32361,
        "type": "I64",
        "unit": "kVarh",
        "gain": 100,
        "quantity": 4,
        "description": "Positive reactive electricity"
    }
}
