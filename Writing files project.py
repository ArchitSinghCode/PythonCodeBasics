#Writing files project
import time

while True:
    file_path = input("Enter the name of the filepath: ")
    txt_data = input("Enter the text data: ")

    try:
        with open(file_path, "x") as file:
            file.write(txt_data)
            print(f"The location '{file_path}' has been created.")
    except FileExistsError:
        print("Sorry! that file already exists!")

    again = input("Would you like to continue(Y/N)? ").lower().strip()
    while again not in ["y","n"]:
        print("Enter a valid input")
        time.sleep(1)
        again = input("Would you like to continue(Y/N)? ").lower().strip()
    if again == "y":
        print("Great, lets carry on!")
        time.sleep(1)
    else:
        print("Alright! Come back later when you're ready!")


