menu = {"pizza" : 3.00,
        "nachos": 5.00,
        "popcorn": 4.50,
        "fries": 2.50,
        "chips": 1.00,
        "soda": 3.00,
        "lemonade": 4.25}

cart= []
total = 0

print("---------MENU---------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}",)
print("---------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total +=  menu.get(food)
    print(food , end=" ")

print()
print(f"total is: ${total:.2f}")
print("-------------------------------")