#Number guessing game
import random
import time
number = random.randint(1,20)
guess = 5
while True:

        if guess ==0:
            print("Game over you ran out of guesses!")
            break

        print(f"You have {guess} guess/s left.")
        user_input = input("Enter a number from 1-20(Q to quit): ").strip().lower()
        if user_input.lower() == "q":
            print("Thank you for playing!")
            time.sleep(1)
            print("Come back when you're ready!")
            break
        try:
            user_guess = int(user_input)
            if user_guess <1 or user_guess >20:
                print("That number is out of range(1,20)!")
                continue
            if user_guess == number:
                print("Yes, you got it right!")
                break
            else:
                print("Sorry, that was not the number.")
                guess -=1
                continue
        except ValueError:
            print("Ensure only numerical values are entered.")




