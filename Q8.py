def bmiCalculator(height: float, weight: float) -> float:
    BMI: float = weight/ (height**2)
    return BMI


height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
print("BMI is:", bmiCalculator(height, weight))
