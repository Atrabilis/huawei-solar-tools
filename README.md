# Huawei Solar Tools

**Huawei Solar Tools** is a Python library for interacting with **Huawei solar inverters, batteries, power meters, and energy management interfaces (EMI)** using **Modbus TCP**.

It provides methods to read and write Modbus registers, retrieve operational data, and interpret register values.

## Functionality
- Establishes **Modbus TCP** communication with Huawei solar devices.
- Reads and writes **Modbus registers**.
- Retrieves device status, operational parameters, and alarms.
- Converts raw register values into structured data.
- Supports multiple devices in parallel.

## Target Users
- **Developers** integrating Huawei solar devices into software systems.
- **System administrators** managing solar installations.
- **Data engineers** handling time-series data from Huawei devices.

## Features

### 📡 Communication
- Modbus TCP client for interacting with Huawei solar equipment.
- Multi-device support.

### 🔍 Data Retrieval
- Reads **real-time data** from inverters, batteries, and meters.
- Fetches **system status, alarms, and operational parameters**.
- Reads **raw registers** and interprets their values.

### 🔧 Register Processing
- Decodes **bitfields, integers, floats, and string registers**.
- Converts raw **Modbus register values** into structured formats.

### 📊 Database Integration (User Implementation)
- Compatible with **ClickHouse** and **InfluxDB** for data storage (not required for core library).


## Installation

Huawei Solar Tools requires **Python 3.9+**.

### Install via PyPI:
```bash
pip install huawei-solar-tools
```

### Install from source:
```
git clone https://github.com/atrabilis/huawei-solar-tools.git
cd huawei-solar-tools
pip install .
```



---

## Usage

The following examples demonstrate how to use the **Huawei Solar Tools** library for basic interactions.  
For more detailed examples, refer to the scripts in the `tests/` directory.

### 1️⃣ Initialize a Connection to a Huawei Inverter

```python
from huawei_solar_tools.devices.inverter import Inverter

# Define connection parameters
host = "192.168.1.100"
port = 502
device_id = 1

# Initialize the inverter
inverter = Inverter(host, port, device_id)

async def main():
    await inverter.connect()
    print(f"Device ID: {inverter.get_device_id()}")
    print("All Registers:", await inverter.read_all_registers())
    await inverter.disconnect()

import asyncio
asyncio.run(main())
```

## Supported Devices and Compatibility

**Huawei Solar Tools** is designed to interact with the following Huawei solar devices via the **Modbus TCP** protocol. Compatibility is based on the firmware and device models specified in the Huawei Modbus documentation.

### 1️⃣ **Inverters**
- **Supported Models**: SUN2000 Series
  - Example Models: SUN2000-33KTL, SUN2000-60KTL, SUN2000-100KTL
- **Firmware Requirements**: V100R001C00SPC200 or later

### 2️⃣ **Batteries**
- **Supported Models**:
  - **LUNA2000**: LUNA2000-5, LUNA2000-10
  - **LG-RESU**: LG-RESU10H
- **Firmware Requirements**: V200R002C10SPC100 or later

### 3️⃣ **Power Meters**
- **Supported Models**:
  - DDSU666-H
  - DTSU666-H
- **Features**:
  - Measures phase voltages, currents, active/reactive power, and total energy.
  - Registers include power factor, phase-by-phase power, and total energy consumption.

### 4️⃣ **Energy Management Interfaces (EMI)**
- **Supported Features**:
  - Environmental monitoring (wind speed, wind direction, temperature, irradiance).
  - Supports data logging and integration with Huawei SmartLogger.
- **Firmware Requirements**: V200R002C20 or later

### 5️⃣ **SmartLogger**
- **Supported Models**:
  - SmartLogger3000
  - SmartLogger2000
- **Firmware Requirements**: V100R001C00 or later
- **Features**:
  - Supports data collection and communication with multiple Huawei devices.
  - Provides power control, alarm management, and device synchronization via Modbus.

### References

1. Huawei Technologies Co., Ltd. *SmartLogger Modbus Interface Definitions, Issue 35*. 2020. [Proprietary documentation](https://e.huawei.com/).
2. Huawei Technologies Co., Ltd. *Solar Inverter Modbus Interface Definitions, Issue 5*. 2020. [Proprietary documentation](https://e.huawei.com/).

## Contributing

Contributions to Huawei Solar Tools are welcome! Follow the steps below to contribute to the project:

| Step                | Description                                                                                  | Commands/Details                                                                                                     |
|---------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **1. Fork**         | Create a personal copy of the repository.                                                   | Click the **Fork** button on the repository's GitHub page.                                                          |
| **2. Clone**        | Clone the forked repository to your local machine.                                          | ```bash<br>git clone https://github.com/YOUR_USERNAME/huawei-solar-tools.git<br>cd huawei-solar-tools<br>```       |
| **3. Branch**       | Create a new branch for your changes.                                                       | ```bash<br>git checkout -b feature-new-functionality<br>```                                                        |
| **4. Develop**      | Make your changes following the current structure and conventions of the codebase.          | - Keep your code readable and consistent.<br>- Add docstrings where appropriate to explain functionality.           |
| **5. Test (if applicable)** | Verify your changes using the provided test scripts in the `tests/` directory or you can make your own less ad hoc more proffesional tests.               | ```bash<br>python tests/test_inverter.py<br>```                                                                     |
| **6. Commit**       | Stage and commit your changes with a descriptive message.                                   | ```bash<br>git add .<br>git commit -m "Add new functionality for inverters"<br>```                                  |
| **7. Push**         | Push your changes to your forked repository.                                                | ```bash<br>git push origin feature-new-functionality<br>```                                                        |
| **8. Pull Request** | Open a pull request to the main repository.                                                 | Provide a clear description of your changes and their purpose.                                                     |

For questions or clarifications, feel free to open an issue.

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software, provided that the original copyright notice and permission notice are included in all copies or substantial portions of the software.

For detailed licensing information, refer to the [LICENSE](LICENSE) file in the repository.

## Future Work

A lot of improvements and features are planned for Huawei Solar Tools like optimizers reading and write operations. A detailed roadmap will be posted in the future.
