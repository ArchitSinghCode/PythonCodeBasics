#NetPriceCalculator

def net_price(list_price,discount,tax):
    return list_price * (1-discount) * (1+tax)

while True:
    try:
        list_price = float(input("Enter the list price: "))
        discount = float(input("Enter the discount percentage: "))
        while discount >100 or discount <0:
            print("Discount must not be greater than 100 or less than 0.")
            discount = float(input("Enter the discount percentage: "))
        discount = discount/100
        tax = float(input("Enter the tax percentage: "))
        while tax >100 or tax <0:
            print("Tax must not be greater than 100 or less than 0.")
            tax = float(input("Enter the tax percentage: "))
        tax = tax/100
        print(f"Your final net price is ${net_price(list_price,discount,tax):.2f}")
    except ValueError:
        print("Please enter a numeric value.")
        continue
    continue_decision = input("Would you like to continue(Y/N)?: ")
    while continue_decision.lower() not in ["y","n"]:
        print("Please enter a valid input(Y/N).")
        continue_decision = input("Would you like to continue(Y/N)?: ")
    if continue_decision.lower() == "y":
        print("Great! lets carry on")
    else:
        print("Alright then come back later when you're ready!")
        break




