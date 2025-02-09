items = []
sold_items = []

names = ["mini pump", "patch kit", "saddle bag"]
quantities = [359, 777, 54]
units = ["pcs", "pcs", "pcs"]
units_price = [22.5, 49.99, 250]

for i in range(len(names)):
    items += [
        {
            "name": names[i],
            "quantity": quantities[i],
            "unit": units[i],
            "unit_price": units_price[i]
        }
    ]


def get_items():
    print("\t\tName \t\t\t Quantity \t\t  Unit \t\t Unit price (PLN)")
    print("-" * 84)
    for element in items:
        name_string = element['name'].center(20)
        quantity_string = str('{:03d}'.format(element['quantity']).center(10))
        unit_string = element['unit'].center(7)
        unit_price_string = str('{:.2f}'.format(element['unit_price']).center(15))
        print(f"{name_string}\t{quantity_string}\t\t{unit_string}\t\t{unit_price_string}")


def add_item():
    print("Adding new item...")
    while True:
        add_item_name = str(input("Enter product's name: "))
        if add_item_name.lower() == "quit":
            print("You have quit.")
            break
        items.append(
            {
                "name": add_item_name,
                "quantity": int(input("Enter product's quantity: ")),
                "unit": str(input("Enter unit's type: ")),
                "unit_price": float(input("Enter product's price per unit: "))
            }
        )
        print()
        print("You have successfully added a new product to the warehouse stock.\nHere's current status:")
        get_items()
        break


def get_costs():
    warehouse_value_total = sum([element['quantity'] * element['unit_price'] for element in items])
    return round(warehouse_value_total, 2)


def sell_item(item_sold, quantity_sold):
    item_found = False
    for element in items:
        if item_sold == element['name']:
            item_found = True
            if int(quantity_sold) <= element['quantity']:
                element['quantity'] = element['quantity'] - int(quantity_sold)
                print(f"{quantity_sold} {element['unit']} of {item_sold} sold.\nHere's current warehouse status:")
                get_items()
                sold_element = {}
                sold_element += {
                    "name": element['name'],
                    "quantity": quantity_sold,
                    "unit": element['quantity'],
                    "unit_price": element['unit_price']
                }
                sold_items.append(sold_element)
                print(sold_items)
            else:
                print(f"There's not enough {item_sold} to sell.")
    if item_found is False:
        print("Such item is not available in the warehouse.")


def get_income():
    income_value_total = sum([element['quantity'] * element['unit_price'] for element in sold_items])
    return round(income_value_total, 2)


def show_revenue():
    print("Revenue breakdown (PLN)")
    revenue_count = get_income() - get_costs()
    print(f"Income: {get_income()} \nCosts: {get_costs()} \nRevenue: {revenue_count}")


welcome = input("What would you like to do?")
while welcome != "exit":
    if welcome == "show":
        get_items()
    elif welcome == "add":
        add_item()
    elif welcome == "sell":
        item_sold = (input("What would you like to sell? "))
        quantity_sold = (input(f"How many pieces of {item_sold} would you like to sell? "))
        sell_item(item_sold, quantity_sold)
    elif welcome == "show_revenue":
        show_revenue()
    else:
        print("This is not a valid input.")
    welcome = input("What would you like to do?")
print("Exiting! Bye...!")
