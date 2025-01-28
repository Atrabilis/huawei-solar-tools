"""
Register Names Generator

This script generates Python files containing constants for register names from dictionaries
defined in the `registers` module. It is designed to automate the creation of constant mappings
for easier and safer access to Modbus registers.

Functionality:
    - Extracts all dictionaries from the `registers` module.
    - Creates a Python file for each dictionary, with constants representing the register names.
    - Outputs the generated files into a specified directory (`registers/` by default).

Usage:
    Run the script directly to generate the constant files:
        python generate_register_names.py

    By default, the script generates files in the `registers/` directory, located in the same
    folder as the script.

Example Output:
    For a dictionary `inverter_registers` with keys `voltage` and `current`, a file
    `inverter_registers.py` will be created with the following content:
        VOLTAGE = "voltage"
        CURRENT = "current"

Dependencies:
    - None (works with standard Python libraries).

Error Handling:
    - Automatically creates the output directory if it doesn't exist.
    - Prints detailed error messages if the generation process fails.
"""

import os
import inspect
import registers

def generate_register_names(output_dir="registers"):
    """
    Generate Python files with constants for register names from dictionaries in the `registers` module.

    :param output_dir: Directory where the generated files will be saved.
    :type output_dir: str
    """
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Extract all dictionaries from the `registers` module
        all_registers = {name: obj for name, obj in inspect.getmembers(registers) if isinstance(obj, dict)}

        for dict_name, reg_dict in all_registers.items():
            # Prepare the content for the file
            lines = [
                f'{name.upper()} = "{name}"' for name in reg_dict.keys()
            ]
            lines.append("")  # Add a trailing newline

            # Write the content to the file
            output_path = os.path.join(output_dir, f"{dict_name}.py")
            with open(output_path, "w") as file:
                file.write("\n".join(lines))

            print(f"File successfully generated: {output_path}")

    except Exception as e:
        print(f"Error generating files: {e}")


if __name__ == "__main__":
    # Default output directory for the generated files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "registers")

    # Generate the files
    generate_register_names(output_dir)
