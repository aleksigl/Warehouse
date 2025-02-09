items = []

names = ["mini pump", "patch kit", "saddle bag"]
quantities = [359, 777, 54]
units = ["pcs", "pcs", "pcs"]
units_price = [22.5, 49.99, 250]

for i in range(len(names)):
    items += [{"name": names[i], "quantity": quantities[i], "unit": units[i], "unit_price": units_price[i]}]


def get_items():
    print("\tName \t\t Quantity \t\t Unit \t\t Unit price (PLN)")
    print("-" * 84)
    for element in items:
        item_details = (
            f"{element['name'].center(20)}\t{str('{:03d}'.format(element['quantity']).center(10))}\t\t{element['unit'].center(7)}\t\t{str('{:.2f}'.format(element['unit_price']).center(15))}")
        print(item_details)


def add_item():
    print("Adding new item...")
    while True:
        add_item_name = str(input("Enter product's name: "))
        element = {}
        if add_item_name.lower() == "quit":
            print("You have quit.")
            break
        element["name"] = add_item_name
        element["quantity"] = int(input("Enter product's quantity: "))
        element["unit"] = str(input("Enter unit's type: "))
        element["unit_price"] = float(input("Enter product's price per unit: "))
        items.append(element)
        print()
        print("You have successfully added a new product to the warehouse stock.\nHere's current status:")
        get_items()
        break


welcome = input("What would you like to do?")
while welcome != "exit":
    if welcome == "show":
        get_items()
    elif welcome == "add":
        add_item()
    else:
        print("This is not a valid input.")
    welcome = input("What would you like to do?")
print("Exiting! Bye...!")
