# Ask user for 2 numbers
# Find if first number tripled is a multiple of the second number doubled
# Print the result

user_number_1 = int(input("Choose the first number:"))
user_number_2 = int(input("Choose the second number"))
tripled = user_number_1 * 3
doubled = user_number_2 * 2

if tripled % doubled == 0:
    print(f"{tripled} is a multiple of {doubled}")
else:
    print(f"{tripled} is not a multiple of {doubled}")