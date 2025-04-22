
"""Title: Even or odd checker"""

# Pseudocode
# Ask user to enter a number
# Once number is entered check if the number is even or odd (use if statements)
# Keep asking until user types "exit"
# if user types "exit" stop program



while True:
    input_number = int(input("Enter a number and i will tell you if its even or odd (Type a negative number to end):"))
    exit_command = "exit"

    if input_number % 2 == 0 and input_number > 0:
        print(f"{input_number} is an even number")

    elif input_number % 2 != 0 and input_number > 0:
        print(f"{input_number} is an odd number")
"""
    if input_number < 0:
        print("bye")
        break"""

