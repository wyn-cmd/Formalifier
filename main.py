# Version 1.0
# 
# A python program that takes informal English and tries to replace informal slang
# and phrases with their formal versions based on a dictionary.


# import modules
import csv


# finds the substring and replaces it with given dictonary
def replace_with_dict(text, replacement_dict):

  for old_str, new_str in replacement_dict.items():
    text = text.replace(old_str, new_str)
  return text


# function to load data from csv file
def load_dict_from_csv(file_path, key_column, value_column):

  result_dict = {}
  with open(file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      result_dict[row[key_column]] = row[value_column]
  return result_dict


# set the csv file
csv_file = 'dict.csv'
key_col = 'Informal'
value_col = 'Formal'

# load the dictionary
replacement_dict = load_dict_from_csv(csv_file, key_col, value_col)

# get user input
text = input('Enter informal text> ')


# formalise the text
result = replace_with_dict(text, replacement_dict)

# print results
print('\n\n----------------------------------------\n')
print(f'Informal:\n\n{text}\n\n')
print('----------------------------------------')
print(f'\n\nFormal:\n\n{result}')
print('\n----------------------------------------')

