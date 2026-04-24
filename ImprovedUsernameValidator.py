#Username validation project
 #Username must not exceed 20 characters
 #Username must contain only letters
 #Username must not contain spaces

while True:
    username = input("Enter username: ")
    if len(username)>20:
        print("Username must not exceed 20 characters.")
        continue
    if not username.rfind(" ") == -1:
        print("Username must not contain spaces.")
        continue
    if  not username.isalpha():
        print("Username must only contain letters: ")
        continue

    print(f"Welcome {username}.")
    break

