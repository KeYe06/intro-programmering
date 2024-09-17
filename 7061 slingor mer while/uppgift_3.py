tal = int(input("Läs in ett tal"))
försök = 1
while tal != 42 and försök < 4:
    if tal < 42:
         tal = int(input("För litet"))
         försök = försök +1
    elif tal > 42:
        tal = int(input("För stort"))
        försök = försök +1
if tal == 42:
    print("Rätt", försök, "försök")
else:
    print ("FÖR MÅNGA FEL")