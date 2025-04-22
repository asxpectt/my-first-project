"Title: Secret Word Hangman"

# Pseudocode
# Create a variable called secret word
# Print blanks representing how many letters the word has
# Ask user to guess a letter
# check if the letter entered is in the word if yes reveal its position
# if not print "Wrong guess!"
# Only allow 5 wrong guesses and then end game


while True:
    secret_word = "nack"
    print("___")
    guess_letter = input("Guess a letter: ")

    position = 0
    for letter in secret_word:
        if letter == guess_letter:
            print("Letter", letter, "is at position", position)

        position += 1












