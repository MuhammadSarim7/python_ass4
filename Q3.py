def areaOfCircle(radius: float) -> float:
    PI: float = 3.14159
    area: float = PI * (radius ** 2 )
    return area


radius = float(input("Enter radius of circle: "))
print("Area of circle is:", areaOfCircle(radius))
