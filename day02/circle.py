# Calculation of the area and circumference of a circle

import math

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))
unit = input("Enter the unit of measurement: ")

# Calculate the area
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Display the result
print(f"The area of the circle with radius {radius} {unit} is {area: .2f} {unit}2")
print(f"The circumference of the circle with radius {radius} {unit} is {circumference: .2f} {unit}")