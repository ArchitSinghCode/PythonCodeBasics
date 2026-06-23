#Reading text files
import time
from logging import exception

while True:
    file_path = input("Enter the name of the file path: ")
    try:
        with open(file_path, "r") as file:
           contents = file.read()
           if contents:
               print(f"Here are the contents found in the file location '{file_path}'.")
               print()
               print(contents)
           else:
               print(f"The location '{file_path}' is empty!'")
    except FileNotFoundError:
        print(f"Sorry, the location '{file_path}' was not found.")
    except PermissionError:
        print(f"Sorry, you do not have permission to view the location '{file_path}'.")
    except Exception as e:
        print(f"Something went wrong, technical details: {e}.")

    again = input("Would you like to read another file?(Y/N)").lower().strip()
    while again not in ["y","n"]:
        print("Enter a valid input.")
        time.sleep(1)
        again = input("Would you like to read another file?(Y/N)").lower().strip()
    if again == "y":
        print("Great, lets continue!")
    else:
        print("Sorry to hear you go.")
        time.sleep(1)
        print("Come back again when you're ready!")
        break




