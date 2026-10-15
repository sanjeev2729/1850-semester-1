# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv
import csv
# Open the file and read the data
try:
    with open("week1.3/session2/task2/3_sales_data/sales.csv") as f:
        reader = csv.reader(f)
        next(reader)  # skip the header row

        total = 0
        count = 0
        largest_amount = 0
        largest_date = ""
        units_per_product = {}

        for row in reader:
            date, product, amount, units, region = row
            amount = float(amount)  # convert amount to float for calculations
            units = int(units)  # convert units to int for calculations
            total += amount
            count += 1

            if amount > largest_amount:
                largest_amount = amount
                largest_date = date

            if product in units_per_product:
                units_per_product[product] += units
            else:
                units_per_product[product] = units

    average =  total / count
    best_widget = max(units_per_product, key=units_per_product.get)
    print(f"Largest sale day: {largest_date} with amount ${largest_amount:.2f}")
    print(f"Average sale amount: ${average:.2f}")
    print(f"Most sold widget: {best_widget} with {units_per_product[best_widget]} units sold")
except FileNotFoundError:
    print("The sales data file was not found. Please check the file path.")


        
        
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows