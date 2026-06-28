import json
import time

def yes_no(prompt):
    while True:
        answer = input(prompt).strip().upper()
        if answer in ("Y", "N"):
            return answer
        print("Please enter Y or N.")
while True:
    file_path = input("Enter the name of the file path: ")
    try:
        with open(file_path,"r") as file:
            content = json.load(file)
            read_all = yes_no("Would you like to read the whole file?(Y/N): ")
            if read_all == "Y":
                print(content)
            else:
                key_value = input("Which specific key would you like to know?: ")
                if key_value in content:
                    print(content[key_value])
                else:
                    print(f"The key '{key_value}' was not found.")

    except FileNotFoundError:
        print(f"The location '{file_path}' was not found.")
    except PermissionError:
        print(f"You do not have permission to read the file '{file_path}'.")
    except Exception as e:
        print(f"Something went wrong. Technical details: {e}.")

    again = yes_no("Would you like to continue(Y/N)?: ")
    if again == "Y":
        print("Great, lets continue!")
        time.sleep(1)
    else:
        print("Sorry to hear you go!")
        time.sleep(1)
        print("Come back later when you're ready!")
        break


