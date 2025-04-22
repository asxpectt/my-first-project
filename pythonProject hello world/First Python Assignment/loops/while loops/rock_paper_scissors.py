"""Title: Rock, Paper, Scissors"""

# Pseudocode
# Create an input variable asking user to choose either rock paper or scissors
# Make the computer also pick one of the three
# Create a print statement that says who wins
# Repeat till user types quit

while True:
    user_input = input("Rock, Paper or Scissors?:")
    user_input = user_input.lower()
    if user_input == "rock":
        computer_input == ""