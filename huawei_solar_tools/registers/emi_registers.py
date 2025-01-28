emi_registers = {
    "wind_speed": {
        "address": 40031,
        "type": "I16",
        "unit": "m/s",
        "gain": 10,
        "quantity": 1,
        "description": "Wind speed (WSP)"
    },
    "wind_direction": {
        "address": 40032,
        "type": "I16",
        "unit": "°",
        "gain": 1,
        "quantity": 1,
        "description": "Wind direction (WD)"
    },
    "pv_module_temperature": {
        "address": 40033,
        "type": "I16",
        "unit": "°C",
        "gain": 10,
        "quantity": 1,
        "description": "PV module temperature"
    },
    "ambient_temperature": {
        "address": 40034,
        "type": "I16",
        "unit": "°C",
        "gain": 10,
        "quantity": 1,
        "description": "Ambient temperature"
    },
    "total_irradiance": {
        "address": 40035,
        "type": "I16",
        "unit": "W/m²",
        "gain": 10,
        "quantity": 1,
        "description": "Total irradiance"
    },
    "daily_irradiation_amount": {
        "address": 40036,
        "type": "U32",
        "unit": "MJ/m²",
        "gain": 1000,
        "quantity": 2,
        "description": "Daily irradiation amount"
    },
    "total_irradiance_2": {
        "address": 40038,
        "type": "I16",
        "unit": "W/m²",
        "gain": 10,
        "quantity": 1,
        "description": "Total irradiance 2"
    },
    "daily_irradiation_amount_2": {
        "address": 40039,
        "type": "U32",
        "unit": "MJ/m²",
        "gain": 1000,
        "quantity": 2,
        "description": "Daily irradiation amount 2"
    },
    "custom_1": {
        "address": 40041,
        "type": "I16",
        "unit": "N/A",
        "gain": 10,
        "quantity": 1,
        "description": "Custom 1"
    },
    "custom_2": {
        "address": 40042,
        "type": "I16",
        "unit": "N/A",
        "gain": 10,
        "quantity": 1,
        "description": "Custom 2"
    },
    "daily_irradiation_amount_kwh": {
        "address": 40043,
        "type": "U32",
        "unit": "kWh/m²",
        "gain": 1000,
        "quantity": 2,
        "description": "Daily irradiation amount (kWh/m²)"
    },
    "daily_irradiation_amount_2_kwh": {
        "address": 40045,
        "type": "U32",
        "unit": "kWh/m²",
        "gain": 1000,
        "quantity": 2,
        "description": "Daily irradiation amount 2 (kWh/m²)"
    }
}
