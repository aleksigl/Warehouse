welcome = input("What would you like to do?")
while welcome == "exit":
    print("Exiting! Bye...!")
    exit()
else:
    print("This is not a valid input.")
    welcome = input("Try again. What would you like to do?")
