items = []

names = ["mini pump", "patch kit", "saddle bag"]
quantities = [359, 777, 54]
units = ["piece", "piece", "piece"]
units_price = [22.5, 49.99, 250]

for i in range(len(names)):
    items += [{"name": names[i], "quantity": quantities[i], "unit": units[i], "unit_price": units_price[i]}]

def get_items():
    print("\tName \t\t Quantity \t\t Unit \t\t Unit price (PLN)")
    print("-" * 84)
    for element in items:
        item_details = (f"{element['name'].center(20)}\t{str('{:03d}'.format(element['quantity']).center(10))}\t\t{element['unit']}\t\t{str('{:.2f}'.format(element['unit_price']).center(15))}")
        print(item_details)

welcome = input("What would you like to do?")
while welcome != "exit":
    if welcome == "show":
        get_items()
    else:
        print("This is not a valid input.")
    welcome = input("What would you like to do?")
print("Exiting! Bye...!")

