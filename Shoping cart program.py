#Shopping cart program
foods = []
prices = []
total = 0

while True:
    try:
        food = input("Enter the food item (Q to quit): ")
        if food.lower() == "q":
            print("Alright, come back later when you're ready!")
            break
        else:
            price = float(input("Enter the price of that item: "))
            foods.append(food)
            prices.append(price)
    except ValueError:
        print("Ensure the price is numerical only.")
        continue


print("-----YOUR CART-----")
for food in foods:
    print(food)
for price in prices:
    total += price
print("-------------------")

print()
print(f"Your total is ${total}.")



