"""Title: Palindrome Detector"""

# Pseudocode
# Ask user to enter a random word
# Use if statement to check if word is same forward and backward
# If it is then print "it's a palindrome! otherwise "Not a palindrome
# Keep asking till they enter stop

while True:
    random_word = input("Enter a word (type quit to end:")
    random_word = random_word.lower()
    length_word = int(len(random_word))
    if random_word == "quit":
        break
    elif random_word == random_word[::-1]:
        print("It is a palindrome!")
    else:
        print("Not a palindrome")