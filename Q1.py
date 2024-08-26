def ageCalculator(currentYear: int, birthYear: int) -> int:
    age: int = currentYear - birthYear
    return age


currentYear = int(input("Enter current year: "))
birthYear = int(input("Enter your birth year: "))
print("Your age is:", ageCalculator(currentYear, birthYear))
