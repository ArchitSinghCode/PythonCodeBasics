#Dictionary = a collection of {key:value} pairs. Ordered and unchangeable.
#No duplicates allowed
#Concession stand program
import time
foods = []
total = 0
menu = {"pizza":5.50,"doughnut":2.00,
        "cupcake": 1.50,"coffee":4.00,
        "ice cream":3.00,"cookie":2.00}
print()
print("Here is the menu: ")
time.sleep(1)
for key, value in menu.items():
    print(f"{key:10}:£{value:.2f}")

while True:
        food = input("Enter the food that you would like. Ensure to spell it correctly(Q to quit): ")
        if food.lower() == "q":
            print("Order complete!")
            break
        while food.lower() not in menu:
            food = input("Enter a valid food item from the menu: ")
        else:
            foods.append(food)
print("-----YOUR ORDER-----")
for food in foods:
    total += menu.get(food) #This gets the price of the food in the menu
    print(food)
print("--------------------")

time.sleep(1)
print()
print(f"Your total is £{total:.2f}.")









