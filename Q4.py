def areaOfCube(length: float) -> float:
    area: float = 6 * (length**2)
    return area


length = float(input("Enter length of the cube: "))
print("Area of cube is", areaOfCube(length))
