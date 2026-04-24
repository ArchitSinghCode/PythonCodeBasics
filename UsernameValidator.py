#Username validation project
 #Username must not exceed 20 characters
 #Username must contain only letters
 #Username must not contain spaces

username = input("Enter your username: ").strip()
if len(username) >20:
    print("Sorry, your username is too long.")
elif not username.isalpha():
    print("Sorry, your username needs to only contain alphanumeric characters.")
elif  not username.find(" ") == -1:
    print("Your username must not contain spaces.")
else:
    print(f"Welcome {username}.")

