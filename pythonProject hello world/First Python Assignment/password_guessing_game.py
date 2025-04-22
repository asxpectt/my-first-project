"""Password Guessing Game

Set a secret password (e.g., "pythonrocks").
Keep asking the user for a password until they enter the correct one.
   2. If they type "quit", end the program with break.
   3. If the password is incorrect, tell them "Wrong! Try   again."
   4. If correct, print "Access granted!" and stop the loop."""

""" Title Password Guessing Game """

# Pseudocode
# Create a variable titled secret_password
# Ask user to input a password till they enter the correct password
# If user enters quit end program with break
# If password is wrong, print("Wrong! Try again.)
# If password is right, print("Access granted!") and use break to stop the loop

secret_password = "pythonrocks"
quit_command = "quit"
password = input("What is the password: ")

if password != secret_password and password != quit_command:

    while password != secret_password and password != quit_command:
        print("Wrong! Try again")
        password = input("What is the password: ")

    if password == secret_password:
        print("Access granted!")
    else:
        print("Yeah quit like the loser you are")






