"""Pick a secret number (e.g., 7).
Keep asking the user to guess the number.
If they guess too high, print "Too high! Try again.".
If they guess too low, print "Too low! Try again.".
If correct, print "Congratulations! You guessed it!" and stop the loop.
If they type "quit", end the game."""

"""Title: Number guessing!!"""

# Pseudocode
# Create a variable for a secret number
# Create an input statement asking the user to guess the secret number
# Create a quit variable
# Create an if statement stating that if they guess to high print "Too high! Try again."
# Create another if statement stating that if they guess too low. print "Too low! Try again."
# Create an if statement saying if they guess the correct answer, print "Congratulations! You guessed it!"
# If they guess correct use a break statement to end
# If they type "quit", also end the game

print("Welcome to my guessing game hehe!")
secret_number = 67
guess_the_number = int(input("Guess the secret Number (Type -1 to end game): "))
quit_command = -1


while True:
    if guess_the_number > secret_number:
        print("Too high! Try again.")
        guess_the_number = int(input("Guess the secret Number (Type -1 to end game): "))

    if guess_the_number == secret_number:
        print("Congratulations! You guessed it!")
        break
    if guess_the_number == quit_command:
        print("Yeah quit like the loser you are")
        break

    if guess_the_number < secret_number and guess_the_number != quit_command:
        print("Too low! Try again.")
        guess_the_number = int(input("Guess the secret Number (Type -1 to end game): "))


