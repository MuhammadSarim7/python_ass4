def temperatureInCelsius(temperatureFahrenheit: float) -> float:
    temperatureCelsius: float
    temperatureCelsius = (temperatureFahrenheit - 32) * 5 / 9
    return temperatureCelsius


def temperatureInFahrenheit(temperatureCelsius: float) -> float:
    temperatureFahrenheit: float
    temperatureFahrenheit = (temperatureCelsius * 9 / 5) + 32
    return temperatureFahrenheit


temperatureCelsius = float(input("Enter temperature in Celsius: "))
temperatureFahrenheit = float(input("Enter temperature in Fahrenheit: "))
print("After Conversion: ")
print("Temperature in Celsius:",  temperatureInCelsius(temperatureFahrenheit), "C")
print("Temperature in Fahrenheit:",
      temperatureInFahrenheit(temperatureCelsius), "F")
