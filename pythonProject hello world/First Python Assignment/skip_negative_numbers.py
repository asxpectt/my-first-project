
"""Title: Skip Negative Numbers"""

# Pseudocode

# Ask user to input 5 numbers
# Create an if statement saying (If the number is negative, skip it using """continue""")
# If number is not negative, Print "Valid number: Then print the number"
# Create a loop to make sure 5 valid numbers are processed

count = 0

while count < 5:
    number = int(input("Enter Five Numbers: "))
    if number < 0:
        continue
    else:
        print(f"Valid Number: {number}")
    count += 1
