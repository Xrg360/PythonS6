def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    elif x == 0 and y != 0:
        return "On y-axis"
    elif x != 0 and y == 0:
        return "On x-axis"
    else:
        return "Origin"

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))
print("Point", (x, y), "is in", find_quadrant(x, y))
