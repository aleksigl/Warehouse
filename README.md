# Warehouse Management System

This script allows you to manage a warehouse by keeping track of items, quantities, prices, and sales transactions.
The system includes functionality to:
1. View the current stock of items.
2. Add new items to the warehouse stock.
3. Sell items and update the stock.
4. Calculate the total costs and income from the sales.
5. Show the overall revenue (income - costs).
6. Export the items and sales to CSV files for backup or further analysis.
7. Load items from a CSV file to restore previous stock data.

# Functions:
- get_items(): Displays the current list of items in the warehouse along with their quantities, units, and unit prices.
- add_item(): Allows the user to add a new item to the warehouse stock, including its name, quantity, unit type, and unit price.
- get_costs(): Calculates and returns the total cost of the current stock based on quantity and unit price.
- sell_item(item_sold, quantity_sold): Reduces the stock of an item based on the quantity sold and records the transaction.
- get_income(): Calculates and returns the total income generated from the sales of items.
- show_revenue(): Displays the income, costs, and overall revenue (income - costs).
- export_items_to_csv(): Exports the current list of items to a CSV file for backup.
- export_sales_to_csv(): Exports the list of sold items to a CSV file for backup.
- load_items_from_csv(file_path, items_list): Loads items from a CSV file to restore the warehouse stock.
- prior_welcome_import(file_path): Loads items from a given CSV file before the program's main menu is displayed.
- main(): The main function of the program, providing an interactive interface for the user to perform actions like showing items, adding items, selling items, showing revenue, saving data, and loading data.

# Usage:
- The program can be run in the terminal, where the user will be prompted with options to interact with the warehouse system.
- The system accepts a CSV file as an argument on startup to load previously saved warehouse data. If no file is provided, the system starts with an empty warehouse.
- Available actions:
    - 'exit': Exits the program.
    - 'show': Displays all items in the warehouse.
    - 'add': Adds a new item to the warehouse.
    - 'sell': Sells an item and reduces the stock.
    - 'show_revenue': Shows the income, costs, and revenue.
    - 'save': Saves the current items and sales to CSV files.
    - 'load': Loads items from the CSV file.

# Note:
- The `load_items_from_csv` function reads items from a CSV file, where the file contains columns for item name, quantity, unit, and unit price.
- All monetary values (e.g., unit prices and costs) are represented in PLN (Polish Zloty).
