print("Rooster Cafe")
name = input("What is your name? ")
print("Hello, " + name + "! Welcome to Cafe Rooster.\n")

menu = ("americano", "mocha", "espresso", "cappuccino", "frappuccino", "latte")
print("So, what would you like on our menu today? Here's what we are serving:\n", menu)

order = input("Please enter your order: ").lower()

price = 0

if order == "frappuccino":
    price = 10
elif order == "mocha":
    price = 6
elif order == "cappuccino":
    price = 12
elif order == "espresso":
    price = 8
elif order == "americano":
    price = 4
elif order == "latte":
    extra_cream = input("Do you want extra cream? (yes/no) ").lower()
    if extra_cream == "yes":
        price = 11
    else:
        price = 6
else:
    print("Sorry, we don't have that here.")
    exit()
print(f"The price for one {order} with extra cream is: ${price}")
try:
    quantity = int(input("How many cups would you like? \n"))
    if quantity < 1:
        print("Please enter a valid quantity (1 or more).")
        exit()
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

total = price * quantity
print("Thank you! Your total is: $", total)
print("Sounds good, " + name + "! We'll have your " + str(quantity) + " " + order + "(s) ready for you in a moment.")