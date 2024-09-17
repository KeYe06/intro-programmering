tal = int(input("Läs in ett tal"))
försök = 0
while tal != 42:
    if tal < 42:
         tal = int(input("För litet"))
         försök = försök +1
    elif tal > 42:
        tal = int(input("För stort"))
        försök = försök +1
print("Rätt", försök, "försök")