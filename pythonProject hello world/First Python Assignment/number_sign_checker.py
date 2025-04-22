"""Number Sign Checker
Write a program that takes a number as input and determines if it is:

Positive

Negative

Zero

Challenge: Add a condition to check if the number is even or odd and print the result alongside the sign."""

# Ask user to input a number
# Find if the number is above zero
# Find if the number is below zero
# Find if number is zero


input_number = int(input("What number do you choose? : "))

if input_number == 0:
    print("This number is zero")
elif input_number < 0:
    print("This number is negative")
elif input_number > 0:
    print("This number is positive")


if input_number % 2 == 0:
    print("This is an even number")

if input_number % 2 != 0:
    print("This is an odd number")


