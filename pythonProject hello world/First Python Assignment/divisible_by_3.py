# Ask user to enter a number
# Check if number is divisible by 3 using the % operator

user_number = int(input("Choose a number and lets see if it is divisible by 3:"))
if user_number % 3 == 0:
    print("The number you chose is divisible by 3")
else:
    print("The number you chose is not divisible by 3")