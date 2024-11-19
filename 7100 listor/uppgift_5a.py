import random
tärningar = []
antal = 0
svar = input("Kasta tärning?")
while svar != "nej":
    for i in range (5):
        tärningar.append(random.randint(1,6))
    for ettor in tärningar:
        if ettor == 1:
            antal = antal + 1
        print("antal ettor", antal)
        svar = input("spela igen?")
