
"Title: Word Scrambler"

 # Pseudocode
 # Create a variable named word
 # Create a variable named word_answer
 # Ask user to guess the word answer
 # If correct print "You got it!"
 # If wrong 3 times, print "Better lucky next time"

count = 0
while True:
    word = "thypno"
    word_answer = "python"
    user_input = input("thypno (Try and rearrange this word to the correct word):")
    if user_input == word_answer:
        print("You got it!")
        print("Number of incorrect attempts:", count)
        break
    else:
        print("Better luck next time")
        count = count + 1