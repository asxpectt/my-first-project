
"""Title: Simple calculator"""
# Pseudocode
# Create 2 variables asking user to enter two numbers
# Create another variable asking user to choose an opera5ion (+, -,*,/)
# print both variables and use the operation on both of them
# repeat till they type quit

while True:
    Number_1 = int(input("Enter a number: "))
    Number_2 = int(input("Enter a number: "))
    operation = input("Enter an operation (Enter ::: to quit) : ")
    if operation == ":::":
        print("Bye")
        break
    if operation == "+":
        print(Number_1 + Number_2)

    elif operation == "-":
        print(Number_1 - Number_2)

    elif operation == "*":
        print(Number_1 * Number_2)

    elif operation == "/":
        print(Number_1 / Number_2)




