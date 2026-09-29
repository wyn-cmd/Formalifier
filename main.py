# Formalifier main script
# Reads an informal text input and translates phrases into formal equivalents using a CSV dictionary.

import csv
import sys
from typing import Dict

CSV_FILE = "dict.csv"
KEY_COL = "Informal"
VALUE_COL = "Formal"


# Load mapping pairs from csv into a dictionary
def load_dict_from_csv(file_path: str, key_column: str, value_column: str) -> Dict[str, str]:
    mapping = {}
    try:
        with open(file_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames or key_column not in reader.fieldnames or value_column not in reader.fieldnames:
                print(f"Error: Missing expected columns '{key_column}' or '{value_column}' in CSV.", file=sys.stderr)
                return {}
            
            for row in reader:
                key = row.get(key_column)
                val = row.get(value_column)
                if key is not None and val is not None:
                    mapping[key] = val
                    
        return mapping
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred while reading '{file_path}': {e}", file=sys.stderr)
    
    return {}


# Replace informal phrases with formal equivalents based on the mapping
def replace_with_dict(text: str, replacement_dict: Dict[str, str]) -> str:
    for old_str, new_str in replacement_dict.items():
        text = text.replace(old_str, new_str)
    return text


def main() -> None:
    replacement_dict = load_dict_from_csv(CSV_FILE, KEY_COL, VALUE_COL)
    if not replacement_dict:
        print("No replacements loaded. Please check your CSV file.", file=sys.stderr)
        sys.exit(1)

    try:
        text = input("Enter informal text> ")
    except (KeyboardInterrupt, EOFError):
        print("\nOperation cancelled.", file=sys.stderr)
        sys.exit(0)

    result = replace_with_dict(text, replacement_dict)

    separator = "-" * 40
    print(f"\n\n{separator}")
    print(f"Informal:\n\n{text}\n")
    print(separator)
    print(f"Formal:\n\n{result}\n")
    print(separator)


if __name__ == "__main__":
    main()