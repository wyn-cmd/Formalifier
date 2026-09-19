import csv
from typing import Dict

def replace_with_dict(text: str, replacement_dict: Dict[str, str]) -> str:
    """Replace informal phrases with formal equivalents based on the provided mapping."""
    for old_str, new_str in replacement_dict.items():
        text = text.replace(old_str, new_str)
    return text

def load_dict_from_csv(file_path: str, key_column: str, value_column: str) -> Dict[str, str]:
    """Load mapping pairs from a CSV file into a dictionary."""
    result_dict = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                result_dict[row[key_column]] = row[value_column]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError as e:
        print(f"Error: Missing expected column in CSV: {e}")
    
    return result_dict

def main():
    # Configuration
    CSV_FILE = 'dict.csv'
    KEY_COL = 'Informal'
    VALUE_COL = 'Formal'

    replacement_dict = load_dict_from_csv(CSV_FILE, KEY_COL, VALUE_COL)
    
    if not replacement_dict:
        print("No replacements loaded. Please check your CSV file.")
        return

    text = input('Enter informal text> ')
    result = replace_with_dict(text, replacement_dict)

    # Output formatting
    separator = '-' * 40
    print(f'\n\n{separator}\n')
    print(f'Informal:\n\n{text}\n\n')
    print(separator)
    print(f'\n\nFormal:\n\n{result}')
    print(f'\n{separator}')

if __name__ == "__main__":
    main()