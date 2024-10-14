tal = int(input("Gissa på talet som jag tänker på"))
gissningar = 0
while tal != 42:
    if tal < 42:
        tal = int(input("för lite, gissa igen"))
    else:
        tal = int(input("för stort, gissa igen"))
    gissningar = gissningar + 1
if tal == 42:
    print("rätt", gissningar, "gissningar")