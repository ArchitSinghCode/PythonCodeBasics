import random
options = ("r","p","s")
while True:
    computer_choice = random.choice(options)
    print("You have 3 options, rock paper and scissors.")
    user_choice = input("Enter your choice(RPS): ")
    while user_choice.lower() not in options:
        user_choice = input("Enter a valid choice (RPS): ")
    if user_choice.lower() == "r" and computer_choice == "p":
        print("Your choice: Rock")
        print("Computer choice = Paper ")
        print("You lose!")
    elif user_choice.lower() == "r" and computer_choice == "r":
        print("Your choice: Rock ")
        print("Computer choice: Rock")
        print("Draw!")
    elif user_choice.lower() == "r" and computer_choice == "s":
        print("Your choice: Rock")
        print("Computer choice: Scissors")
        print("You win!")
    elif user_choice.lower() == "p" and computer_choice == "r":
        print("Your choice: Paper")
        print("Computer choice: Rock")
        print("You win!")
    elif user_choice.lower() == "p" and computer_choice == "p":
        print("Your choice: Paper")
        print("Computer choice: Paper")
        print("Draw!")
    elif user_choice.lower() == "p" and computer_choice == "s":
        print("Your choice: Paper")
        print("Computer choice: Scissors")
        print("You lose!")
    elif user_choice.lower() == "s" and computer_choice == "r":
        print("Your choice: Scissors")
        print("Computer choice: Rock")
        print("You lose!")
    elif user_choice.lower() == "s" and computer_choice == "p":
        print("Your choice: Scissors")
        print("Computer choice: Paper")
        print("You win!")
    elif user_choice.lower() == "s" and computer_choice == "s":
        print("Your choice: Scissors")
        print("Computer choice: Scissors")
        print("Draw!")
    again = input("Would you like to continue(y/n): ")
    while again.lower() not in ["y","n"]:
        again = input("Enter a valid input. Would you like to continue(y/n): ")
    if again.lower() == "y":
        print("Great! lets carry on")
        continue
    else:
        print("Alright, come back again when you're ready!")
        break














