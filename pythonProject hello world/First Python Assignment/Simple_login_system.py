"""Title: Simple login system"""

# Pseudocode
# Create 2 dictionaries for 2 user names and 2 passwords
# Create an input statement asking the user for a username
# Create another input statement asking the user for a password
# If user is correct print "Login successful"
# If user is wrong allow the user 3 tries before locking and ending the program.

count = 0
while True:

    my_dict1 = {
        "username": "bring",

    }

    my_dict2 = {

        "password": "bring222",

    }

    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == my_dict1["username"] and password == my_dict2["password"]:
        print("Login successful")
        break
    else:
        count += 1
        print("Wrong Credentials. Try again!")
        if count == 3:
            print("Too many failed attempts")
            print("bye loser")
            break
