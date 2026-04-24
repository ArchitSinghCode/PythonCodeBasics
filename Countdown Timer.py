import time
def countdown_timer(seconds,message):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -=1
    print(message)

while True:
    try:
        time_left = int(input("Enter the number of seconds: "))
        while time_left <=0:
            print("Enter a valid number of seconds.")
            time_left = int(input("Enter the number of seconds: "))
        end_message = input("Enter the end message: ")
        countdown_timer(time_left,end_message)
    except ValueError:
        print("Please enter a numeric value.")
        continue
    again = input("Do you want to continue? (y/n): ")
    while again.lower() not in ["y","n"]:
        again = input("Do you want to continue? (y/n): ")
    if again.lower() == "y":
        print("Great lets carry on!")
    else:
        print("Goodbye!")
        break





