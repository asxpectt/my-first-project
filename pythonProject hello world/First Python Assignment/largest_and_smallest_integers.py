# Ask user for 5 integers
# find and print largest and smallest integers


user_input_1 = int(input("Choose your first number: "))
user_input_2 = int(input("Choose your second number: "))
user_input_3 = int(input("Choose your third number: "))            # Input Numbers
user_input_4 = int(input("Choose your fourth number: "))
user_input_5 = int(input("Choose your fifth number: "))


largest = user_input_1
smallest = user_input_1


if user_input_2 > largest:
    largest = user_input_2
if user_input_3 > largest:
    largest = user_input_3
if user_input_4 > largest:
    largest = user_input_4
if user_input_5 > largest:
    largest = user_input_5


if user_input_2 < smallest:
    smallest = user_input_2
if user_input_3 < smallest:
    smallest = user_input_3
if user_input_4 < smallest:
    smallest = user_input_4
if user_input_5 < smallest:
    smallest = user_input_5


print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")