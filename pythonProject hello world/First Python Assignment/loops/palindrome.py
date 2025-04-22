

# Ask the user to enter a five-digit number.
# Check if number is five digits long. If it's not tell the user there is an error
# Turn number into a string.
# Compare the first and last digits then compare the second and fourth digits
# If the digits don't match then it's not a palindrome
# If the digits matched then it is a palindrome
# Then tell the user whether the number is a palindrome or not

user_input = int(input("Enter a five digit number: "))
number_to_string = str(user_input)
length = len(str(user_input))
if length == 5:
    print("Length Is 5 digits long")
else:
    print("There is an error")

user_input = str(user_input)

if user_input[0] == user_input[4] and user_input[1] == user_input[3]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome")




