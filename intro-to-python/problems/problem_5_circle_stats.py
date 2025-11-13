"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""


def area(r):
    return 3.14 * r * r


def circumference(r):
    return 2 * 3.14 * r


radius = float(input("Circle radius: "))

print(f"Area: {area(radius)}")  # <-- Call the area function and print the result
print(
    f"Circumference: {circumference(radius)}"
)  # <-- Call the circumference function and print
