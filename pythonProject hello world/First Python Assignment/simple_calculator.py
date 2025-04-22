"""Question 4  (Bonus) or (Optional)
Simple Calculator
Write a program that acts as a simple calculator. It should:

Ask the user to input two numbers.

Ask the user to choose an operation (addition, subtraction, multiplication, or division).

Perform the selected operation and print the result.

Challenge: Add a condition to check if the user is trying to divide by zero. If so, print "Cannot divide by zero." """

# Ask user to input 2 numbers
# Ask the user to choose an operation


user_number_1 = int(input("Pick first number : "))
user_number_2 = int(input("Pick second number : "))
operator = input("Choose an operator : ")

addition = "+"
subtraction = "-"
multiplication = "*"
division = "/"

if operator == addition:
    print(f"First number chosen and second number chosen added gives you ,: {user_number_1 + user_number_2}")
elif operator == subtraction:
    print(f"First number chosen and second number chosen subtracted gives you,: {user_number_1 - user_number_2}")
elif operator == division:
    print(f"First number chosen and second number chosen divided gives you,: {user_number_1 // user_number_2}")
elif operator == multiplication:
    print(f"First number chosen and second number chosen multiplied gives you,: {user_number_1 * user_number_2}")
elif user_number_2 == 0 and operator == division:
    print("Sorry we are not available at this time to divide by 0")
elif user_number_1 == 0 and operator == division:
    print("Sorry we are not available at this time to divide by 0")
else:
    print("Invalid Input")







