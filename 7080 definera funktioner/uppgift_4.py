def celtofah(celcius):
    return (9/5) * celcius + 32
def fahtocel(fahrenheit):
    return (5/9) * (fahrenheit - 32)
def keltofah(kelvin):
    return (9/5) * (kelvin - 273.15) + 32
def keltocel(kelvin):
    return celcius - 273.15
def celtokel(celcius):
    return celcius + 273.15
def fahtokel(fahrenheit):
    return (5/9) * (fahrenheit - 32) + 273.15
svar = input("Vill du konvertera temperaturer? j/n")
while svar != "n":
    con = input("Konvertera temperaturer. c = celcius, f = fahrenheit, k = kelvin. Exempel: ctf = celcius to fahrenheit")
    if con == "ctf":
        celcius = float(input("Ange temperatur i celcius"))
        print(celtofah(celcius))
    if con == "ftc":
        fahrenheit = float(input("Ange temperatur i fahrenheit"))
        print(fahtocel(fahrenheit))
    if con == "ktf":
        kelvin = float(input("Ange temperatur i kelvin"))
        print(keltofah(kelvin))
    if con == "ktc":
        kelvin = float(input("Ange temperatur i kelvin"))
        print(keltocel(kelvin))
    if con == "ctk":
        celcius = float(input("Ange temperatur i celcius"))
        print(celtokel(celcius))
    if con == "ftk":
        fahrenheit = float(input("Ange temperatur i fahrenheit"))
        print(fahtokel(fahrenheit))
    svar = input("Konvertera igen? j/n")
print("Stick härifrån")
