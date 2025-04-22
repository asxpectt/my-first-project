""" Title: Multiplication Table Generator """


# Pseudocode
# Create an input statement asking user for a number
# Keep running until they enter exit
def print_multiplication():
    while True:
        user_input = int(input("Type a number (Type -1 to quit): "))
        if user_input == -1:
            break
        for number in range (0,13,1):
            print(f"{number} * {user_input} = {user_input * number}")



print_multiplication()
