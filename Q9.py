def volumeOfCylinder(radius: float, height: float) -> float:
    PI: float = 3.14159
    volume: float = PI * (radius**2)*height
    return volume


radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))
print("Volume of Cylinder is", volumeOfCylinder (radius, height))
