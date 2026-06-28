import csv
import time

def yes_no(prompt):
    while True:
        answer = input(prompt).strip().upper()
        if answer in ("Y","N"):
            return answer
        print("Invalid input, please enter 'Y' or 'N'.")
        time.sleep(1)

while True:
    try:
        file_path = input("Enter the file path: ")
        with open(file_path,"r") as file:
            content = list(csv.reader(file))
            read_all = yes_no("Would you like to read the entire file?(Y/N) ")
            if read_all == "Y":
                for row in content:
                    print(" | ".join(row))
            else:
                try:
                    line = int(input("Which line would you like to read(starting from line 1)? "))-1
                    if 0 <= line < len(content):
                        print(" | ".join(content[line]))
                    else:
                        print("Sorry, that is not a valid line number.")
                except ValueError:
                    print("Please enter a valid line number.")

    except FileNotFoundError:
        print(f"The location '{file_path}' was not found.")
    except PermissionError:
        print(f"You do not have permission to view the location '{file_path}'.")
    except Exception as e:
        print(f"You cannot view the location '{file_path}'.")
        time.sleep(1)
        print(f"Technical details: {e}.")

    again = yes_no("Do you want to continue(Y/N)? ")
    if again == "Y":
        print("Great, lets continue!")
        print()
    else:
        print("Sorry to hear that.")
        time.sleep(1)
        print("Come back later when you're ready!")
        break

