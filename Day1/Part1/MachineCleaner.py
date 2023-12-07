file_path = '/Users/hampusandersson/Documents/VscodeProjects/AdventOfCode2024/Day1/puzzleinput.txt'

def extract_two_digit_number(line):
    digits = [char for char in line if char.isdigit()]
    if len(digits) >= 2:
        return digits[0] + digits[-1]  # First and last digit
    elif len(digits) == 1:
        return digits[0] * 2  # Duplicate the single digit
    else:
        return None  # Handle lines with no digits

total_sum = 0

with open(file_path, 'r') as file:
    for line in file:
        two_digit_number = extract_two_digit_number(line.strip())
        if two_digit_number:
            total_sum += int(two_digit_number)  # Add the two-digit number to the total sum

print(total_sum)  # Print the total sum of all two-digit numbers
