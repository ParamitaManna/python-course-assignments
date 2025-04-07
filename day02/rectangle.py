# Calculation of the area and perimeter of a rectangle

import math

# Get the parameters from the user
length = float(input("Enter the height of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
unit = input("Enter the unit of measurement: ")

# Calculate the area and the perimeter
area = length * width
perimeter = 2 * (length + width)

# Display the results
print(f"The area of the rectangle is {area: .2f} {unit}2")
print(f"The perimeter of the rectangle is {perimeter: .2f} {unit}")