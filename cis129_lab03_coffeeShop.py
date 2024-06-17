# CIS 129 Lab 3 Coffee Shop Simulator
# This program calculates the total cost of an order per customer input based on item and quantity requested
# Zach Alderete
# 6/16/2024
# Add two more items to menu
# Add a message at the end of the program to thank the user

# Prices per item offered
coffee_price = 5.00
muffin_price = 4.00
tea_price = 7.00
pie_price = 9.00
tax_rate = 0.06

# Start receipt and get the number of items requested from user and convert to integer for calculations
print("***************************************")
print("My Coffee and Muffin Shop")
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_teas = int(input("Number of teas bought? "))
num_pies = int(input("Number of pies bought? "))
print("***************************************")

# Calculate the costs
subtotal_coffee = num_coffees * coffee_price
subtotal_muffin = num_muffins * muffin_price
subtotal_teas = num_teas * tea_price
subtotal_pies = num_pies * pie_price
subtotal = subtotal_coffee + subtotal_muffin + subtotal_teas + subtotal_pies
tax = subtotal * tax_rate
total = subtotal + tax

# Print the remaining receipt
print()
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(str(num_coffees) + " Coffees at $" + format(coffee_price, ".2f") + " each: $ " + format(subtotal_coffee, ".2f"))
print(str(num_muffins) + " Muffins at $" + format(muffin_price, ".2f") + " each: $ " + format(subtotal_muffin, ".2f"))
print(str(num_teas) + " Teas at $" + format(tea_price, ".2f") + " each: $ " + format(subtotal_teas, ".2f"))
print(str(num_pies) + " Pies at $" + format(pie_price, ".2f") + " each: $ " + format(subtotal_pies, ".2f"))  
print("6% tax: $ " + format(tax, ".2f"))
print("---------")
print("Total: $ " + format(total, ".2f"))
print("***************************************")
print("Thank you for coming in, hope to see you again soon!")
