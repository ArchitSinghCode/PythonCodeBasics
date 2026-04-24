import random
import time
def validator(reel1,reel2,reel3,score):
    if reel1 == reel2 and reel1 == reel3 and reel2 == reel3:
        print("Well done, you won!")
        return score+2

    elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
        print("You scored one point!")
        return score+1

    else:
        print("You lose!")
        return score-1


def play_game():
    score = 0
    while True:
        time.sleep(1)
        fruit = ["Apple","Banana","Pear","Orange","Strawberry"]
        dice = random.randint(0,4)
        reel1 = fruit[dice]

        dice = random.randint(0,4)
        reel2 = fruit[dice]

        dice = random.randint(0,4)
        reel3 = fruit[dice]
        print(reel1, reel2, reel3)
        print()
        score = validator(reel1,reel2,reel3,score)
        print(f"Your score is {score}.")

        again = input("Would you like to play again?(Y/N) ").lower().strip()
        while again not in ["y","n"]:
            print("That was not a valid input.")
            time.sleep(1)
            again = input("Would you like to play again?(Y/N) ").lower().strip()
        if again == "y":
            print("Great, lets carry on!")
        else:
            print("Sorry to hear that!")
            break

play_game()



