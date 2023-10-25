import turtle
import random

# Create a turtle object
t = turtle.Turtle()

# Prompt the user for input, ensuring the correct input format
# The input should be a positive integer between 1 and 10
# This determines the number of shapes to draw
n = int(input("How many shapes do you want to draw? (Enter a number between 1 and 10): "))
while n < 1 or n > 10:
    print("Invalid input. Please enter a number between 1 and 10.")
    n = int(input("How many shapes do you want to draw? (Enter a number between 1 and 10): "))

# Use the input value to create a visually appealing picture with multiple shapes of different colors and layouts
# Use a list of colors to choose from
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Use a for loop to draw n shapes
for i in range(n):
    # Choose a random color from the list
    color = random.choice(colors)

    # Set the turtle's color and fill color to the chosen color
    t.color(color)
    t.fillcolor(color)

    # Use an if statement to alternate between drawing circles and squares
    if i % 2 == 0:
        # Draw a circle with a random radius between 50 and 100 pixels
        radius = random.randint(50, 100)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
    else:
        # Draw a square with a random side length between 50 and 100 pixels
        side = random.randint(50, 100)
        t.begin_fill()
        for j in range(4):
            t.forward(side)
            t.right(90)
        t.end_fill()

    # Move the turtle to a random position on the screen
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.up()
    t.goto(x, y)
    t.down()

# Hide the turtle when done
t.hideturtle()