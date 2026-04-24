import os
while True:

     file_name = input("Enter the name of the file: ")

     if os.path.exists(file_name):
        print(f"The file '{file_name}' exists.")

        if os.path.isfile(file_name):
            print(f"The file '{file_name}' is a file.")
        elif os.path.isdir(file_name):
            print(f"The file '{file_name}' is a directory.")
     else:
        print(f"The file '{file_name}' does not exist.")

     again = input("Would you like to continue(Y/N)? ").lower().strip()
     while again not in ["y","n"]:
         again = input("Enter a valid input. Would you like to continue(Y/N)? ").lower().strip()
     if again == "y":
         print("Great lets carry on!")
         continue
     else:
         print("Alright then, come back later when you're ready!")
         break





