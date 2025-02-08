items = []

names = ["mini pump", "patch kit", "saddle bag"]
quantities = [359, 777, 54]
units = ["piece", "piece", "piece"]
units_price = [22.5, 49.99, 250]
for i in range(len(names)):
    items = [{"name": names[i], "quantity": quantities[i], "unit": units[i], "unit_price": units_price[i]}]

welcome = input("What would you like to do?")
while welcome == "exit":
    print("Exiting! Bye...!")
    exit()
if welcome == "show":
    get_items()
    welcome = input("What would you like to do next?")
else:
    print("This is not a valid input.")
    welcome = input("Try again. What would you like to do?")

