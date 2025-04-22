"""Title: Find the First Even Number """

# Pseudocode

# Create an input variable
# Loop the input variable (Ask user to keep inputting numbers)
# Create a condition (If user enters an even number, stop asking user to input numbers)
# If user enters an even number print the following:
# "Found an even number: Print the number they entered
# If the number is odd, tell user to try again

"""even_number_finder = int(input("Input a number:"))


while even_number_finder % 2 == 0:
    print("Found an even number")
    break
else:
    print("Number is odd, try again")
"""

while True:
    even_number_finder = int(input("Input a number:"))
    if even_number_finder % 2 == 0:
        print("Found an even number")
        break
    else:
        if even_number_finder % 2 != 0:
            print("Number is odd, try again")