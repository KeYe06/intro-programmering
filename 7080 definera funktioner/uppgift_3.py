def keltofah(kelvin):
    return (9/5) * (kelvin - 273.15) + 32
kelvin = float(input("Ange temperatur i kelvin"))
print(keltofah(kelvin))