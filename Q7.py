def percentageCalculator(numerator: float, denominator: float) -> float:
    percentage: float = (numerator*100)/denominator
    return percentage


numerator = float(input("Enter numerator: "))
denominator = float(input("Enter denominator: "))
print("Percentage is", percentageCalculator(numerator, denominator), "%")
