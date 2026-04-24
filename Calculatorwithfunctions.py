def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

while True:
    try:
        operator = input("Enter an operator(+-*/): ")
        while operator not in ["+","-","*","/"]:
            operator = input("Enter a valid operator(+-*/): ")
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        if operator == "+":
            print(f"The result is {add(x,y):.2f}.")
        elif operator == "-":
            print(f"The result is {subtract(x,y):.2f}.")
        elif operator == "*":
            print(f"The result is {multiply(x,y):.2f}.")
        elif operator == "/":
            print(f"The result is {divide(x,y):.2f}.")
    except ValueError:
        print("All values must be entered in number.")
    except ZeroDivisionError:
        print("Division by zero is not mathematically possible!")
    continue_decision = input("Would you like to continue?(Y/N): ")
    while continue_decision.lower() not in ["y","n"]:
        print("Please enter a valid input.")
        continue_decision = input("Would you like to continue?(Y/N): ")
    if continue_decision.lower() == "y":
        print("Great! lets carry on.")
    else:
        print("Alright then. Come back when you're ready!")
        break

