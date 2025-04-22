# Tell user to input a password
# Check if password contains one uppercase letter, one lowercase letter, and one digit.
#Check if it contains at least one special character
#Print "Strong password" if all conditions are met
#If not print "Weak password"

import string

password = input("What is your password? :")
special_characters = list(string.punctuation)
uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)
numbers_list = list("0123456789")





