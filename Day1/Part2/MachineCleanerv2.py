file_path = '/Users/hampusandersson/Documents/VscodeProjects/AdventOfCode2024/Day1/puzzleinput.txt'

# Mapping of textual representations of numbers to their numeric equivalents
number_translations = {
    "oneight": "18", "twone": "21", "threeight": "38", "fiveight": "58",
    "sevenine": "79", "eightwo": "82", "eighthree": "83", "nineight": "98",
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

def convert_line_to_digits(line):
    # Replace textual numbers with digits
    for text, digit in number_translations.items():
        line = line.replace(text, digit)

    # Extract digits from the line
    extracted_digits = [char for char in line if char.isdigit()]

    # Construct a two-digit number from the extracted digits
    if len(extracted_digits) >= 2:
        return extracted_digits[0] + extracted_digits[-1]  # First and last digit
    elif extracted_digits:
        return extracted_digits[0] * 2  # Repeat the digit if only one is found
    else:
        return '00'  # Return '00' if no digits are found

# Summing up all the two-digit numbers from the file
with open(file_path, 'r') as file:
    total_sum = sum(int(convert_line_to_digits(line.strip().lower())) for line in file)

print(total_sum)
