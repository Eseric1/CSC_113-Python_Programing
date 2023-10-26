# Import the turtle module
import turtle
import random

# Prompts for input to draw cirlce, square or triangle, ensuring the correct input format
shape = input("What kind of shape do you want to draw? (Enter circle, triangle or square): ")
while shape not in ["circle", "triangle", "square"]:
    print("Invalid input. Please enter circle, triangle or square.")
    shape = input("What kind of shape do you want to draw? (Enter circle, triangle or square): ")

# Prompt for input about how many of those shapes to draw between 1 and 10, ensuring the correct input format
n = int(input("How many shapes do you want to draw? (Enter a number between 1 and 10): "))
while n < 1 or n > 10:
    print("Invalid input. Please enter a number between 1 and 10.")
    n = int(input("How many shapes do you want to draw? (Enter a number between 1 and 10): "))

# Colors available
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Create a turtle object set speed 
t = turtle.Turtle()
t.speed(4)

# Background color to black
turtle.bgcolor("black")

# For loop to draw n shapes with different colors and sizes
for i in range(n):
    # Choose a color from the list 
    color = colors[i % len(colors)]

    # Set the turtle's color and fill color 
    t.color(color)
    t.fillcolor(color)

    # Use an if statement to draw different shapes based on the input value
    if shape == "circle":
        # Draw a circle with random sizes
        radius = random.randint(25,75)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

    elif shape == "triangle":
        # Draw an triangle with random sizes
        side = random.randint(50,150)
        t.begin_fill()
        for j in range(3):
            t.forward(side)
            t.left(120)
        t.end_fill()

    else:
        # Draw a square with random sizes
        side = random.randint(50, 150)
        t.begin_fill()
        for j in range(4):
            t.forward(side)
            t.right(90)
        t.end_fill()

    # Move turtle to random spots
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.up()
    t.goto(x, y)
    t.down()
    

# Hide the turtle when done then exit on click
t.hideturtle()
turtle.exitonclick()
