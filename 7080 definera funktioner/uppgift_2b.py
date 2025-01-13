def fartocel(fahrenheit):
    return (5/9) * (fahrenheit - 32)

fahrenheit = float(input("Ange temperatur i fahrenheit"))
print(fartocel(fahrenheit))