# Create an input variable that asks user for a number 1-7
#Make the number print the days of the week
#Monday being 1 and Sunday being 7
#Check if input number is valid

user_input = int(input("Enter a number between 1-7: "))
if user_input == 1:
    print("Monday")
elif user_input == 2:
    print("Tuesday")
elif user_input == 3:
    print("Wednesday")
elif user_input == 4:
    print("Thursday")
elif user_input == 5:
    print("Friday")
elif user_input == 6:
    print("Saturday")
elif user_input == 7:
    print("Sunday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")






