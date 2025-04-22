# Ask user to enter a number
"""Find if the number entered and the square of number
entered are greater than, equal to, not equal to, or less than the number 100"""



user_number = int(input("Enter a number: " ))
user_number_square = user_number*user_number
if user_number > 100 and user_number_square > 100:
    print(f"number entered {user_number} is greater than 100")

if user_number == 100 and user_number_square == 100:
    print(f"number entered {user_number} is equal to 100")

if user_number != 100 and user_number_square != 100:
    print(f"number entered {user_number} is not equal to 100")

if user_number < 100 and user_number_square < 100:
    print(f"number entered {user_number}  is less than 100")

if user_number == 100 and user_number_square > 100:
    print(f"number entered squared {user_number} is greater than 100 {user_number_square}")




