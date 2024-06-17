# CIS 129 Lab 3 Coffee Shop Simulator
# This program calculates the total cost of an order per customer input
# Zach Alderete
# 6/16/2024

# Prices per item offered
coffee_price = 5.00
muffin_price = 4.00
tax_rate = 0.06

# Get the number of items requested from user and convert to integer for calculations
print("***************************************")
print("My Coffee and Muffin Shop")
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
print("***************************************")

# Calculate the costs
subtotal_coffee = num_coffees * coffee_price
subtotal_muffin = num_muffins * muffin_price
subtotal = subtotal_coffee + subtotal_muffin
tax = subtotal * tax_rate
total = subtotal + tax

# Print the receipt
print()
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(str(num_coffees) + " Coffees at $" + format(coffee_price, ".2f") + " each: $ " + format(subtotal_coffee, ".2f"))
print(str(num_muffins) + " Muffins at $" + format(muffin_price, ".2f") + " each: $ " + format(subtotal_muffin, ".2f"))
print("6% tax: $ " + format(tax, ".2f"))
print("---------")
print("Total: $ " + format(total, ".2f"))
print("***************************************")
