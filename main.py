import csv
import sys
from typing import Dict

CSV_FILE = "dict.csv"
KEY_COL = "Informal"
VALUE_COL = "Formal"


# load mapping pairs from csv into a dictionary
def load_dict_from_csv(file_path: str, key_column: str, value_column: str) -> Dict[str, str]:
    try:
        with open(file_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            return {row[key_column]: row[value_column] for row in reader}
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.", file=sys.stderr)
    except KeyError as e:
        print(f"Error: Missing expected column in CSV: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
    
    return {}


# replace informal phrases with formal equivalents based on the mapping
def replace_with_dict(text: str, replacement_dict: Dict[str, str]) -> str:
    for old_str, new_str in replacement_dict.items():
        text = text.replace(old_str, new_str)
    return text


def main() -> None:
    replacement_dict = load_dict_from_csv(CSV_FILE, KEY_COL, VALUE_COL)
    if not replacement_dict:
        print("No replacements loaded. Please check your CSV file.", file=sys.stderr)
        sys.exit(1)

    text = input("Enter informal text> ")
    result = replace_with_dict(text, replacement_dict)

    separator = "-" * 40
    print(f"\n\n{separator}")
    print(f"Informal:\n\n{text}\n")
    print(separator)
    print(f"Formal:\n\n{result}\n")
    print(separator)


if __name__ == "__main__":
    main()