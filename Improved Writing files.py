#Improved writing files

import time
while True:
    file_name = input("Enter the name of the location: ")
    time.sleep(1)
    txt_data = input("Enter the text data: ")
    try:
         with open(file_name, "x") as file:
            file.write("\n"+ txt_data)
            print(f"The location '{file_name}' has been updated successfully.")
    except FileExistsError:
        print("Oops, that file already exists!")
        time.sleep(1)
        choice = input("Would you like to append this file instead? (Y/N): ").lower().strip()
        while choice not in ["y","n"]:
            print("That's not a valid input!")
            time.sleep(1)
            choice = input("Would you like to append this file? (Y/N): ")
        if choice == "y":
            with open(file_name, "a") as file:
                file.write("\n"+txt_data)
                print(f"The location '{file_name}' has been updated successfully.")
        else:
            print(f"No changes were made to '{file_name}'." )

    decision = input("Would you like to continue? (Y/N): ").lower().strip()
    while decision not in ["y","n"]:
        print("That's not a valid input!")
        time.sleep(1)
        decision = input("Would you like to continue? (Y/N): ").lower().strip()
    if decision == "y":
        print("Great! Lets continue!")
    else:
        print("Alright, come back later when you're ready!")
        time.sleep(1)
        break











