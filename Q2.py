def areaOfRectangle(length: float, width: float) -> float:
    area: float = length * width
    return area


length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("Area of rectangle is: ", areaOfRectangle(length, width))
