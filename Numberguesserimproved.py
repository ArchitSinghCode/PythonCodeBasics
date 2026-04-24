#Improved number guessing game
import random

def play_game():
    while True:
        number = random.randint(1, 20)
        guesses_left = 5
        print("I'm thinking of a number between 1-20. Lets see if you can guess it.")

        while guesses_left >0:
            print(f"You have {guesses_left} guess(es) left.")
            user_input = input("Enter a number to guess(Q to quit): ").lower().strip()
            if user_input == "q":
                print("Goodbye!")
                return
            try:

                user_guess = int(user_input)
                if user_guess <1 or user_guess >20:
                    print("Sorry, that number is outside the range(1,20).")
                    continue
                elif user_guess == number:
                    print("Hooray! You guessed the number correctly!")
                    break
                else:
                    guesses_left -=1
                    print("Sorry, that was not the number.")

            except ValueError:
                print("Please enter a numeric value or Q to quit.")

        if guesses_left == 0:
            print(f"Game over. The number was {number}.")

        again = input("Would you like to continue(Y/N): ").lower().strip()
        while again not in ["y", "n"]:
            print("Please enter a valid input.")
            again = input("Would you like to continue(Y/N): ").lower().strip()
        if again == "y":
            print("Great, lets carry on!")
        else:
            print("Alright, come back again when you're ready!")
            break


if __name__ == "__main__":
    play_game()







