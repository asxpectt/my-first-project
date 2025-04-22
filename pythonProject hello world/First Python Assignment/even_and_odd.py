#Asks the user for 2 numbers
#If any numbers are even or odd
#If number entered is even multiply the number by itself and show the result
#If the even number multiplied
#Do the same thing for the odd numbers

user_first_number = int(input("Choose the first number:"))
user_second_number = int(input("Choose the second number:"))
first_number_multiplied = user_first_number * user_first_number

if user_first_number % 2 == 0:
    print(f"{user_first_number} is an even number")
else:
    print(f"{user_first_number} is an odd number")

if user_second_number % 2 == 0:
    print(f"{user_second_number} is an even number")
else:
    print(f"{user_second_number} is an odd number")

if user_first_number % 2 == 0:
    print(f"The number multiplied by it self is {user_first_number*user_first_number} and it is an even number")

if user_second_number % 2 == 0:
    print(f"The number multiplied by it self is {user_second_number* user_second_number} and it is an even number")





