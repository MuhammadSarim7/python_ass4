def secondsConverter(seconds: int):
    minutes: int = seconds // 60
    sec: int = seconds % 60
    return f"{minutes} min {sec} s"


seconds = int(input("Enter number of seconds: "))
print("Conversion:", secondsConverter(seconds))
