#Miles-per-Gallon

# Number of miles driven
miles = float(input("Enter the number of miles driven: "))

# Gallons of gas used
gallons = float(input("Enter the gallons of gas used: "))

# Calculate the car's MPG using the formula
mpg = miles / gallons

# Display the result
print(f"The car's MPG is {mpg:.2f}")


##Tip, Tax, and Total

# Charge for the food
food_cost = float(input("Enter the charge for the food: "))

tip = food_cost * 0.18
tax = food_cost * 0.07

# Calculate the total amount of the meal
total = food_cost + tip + tax

# Display each of these amounts and the total
print(f"The tip is ${tip:.2f}")
print(f"The tax is ${tax:.2f}")
print(f"The total is ${total:.2f}")