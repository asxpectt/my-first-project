"""Title: Word Reverser"""

# Pseudocode
# Create an input statement asking user to enter a word
# Print the word using ::-1
# repeat this till user quits

print("Welcome to my word reverser game")


while True:
    input_statement = input("Enter a word: ")
    if input_statement == "quit":
        break
    else:
        print(input_statement[::-1])


