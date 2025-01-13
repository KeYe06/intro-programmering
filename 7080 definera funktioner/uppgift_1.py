def tempex(celcius):
    return celcius - 273.15
celcius = float(input("Ange temperatur i kelvin"))
print("Temperatur i celcius är:", tempex(celcius), "C")