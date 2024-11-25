import random
tärningar = []
antal = 0
antal2 = 0
antal3 = 0
antal4 = 0
antal5 = 0
antal6 = 0
svar = input("Vill du spela?")
while svar != "nej":
    for i in range (5):
        tärningar.append(random.randint(1, 6))
    for sak in tärningar:
        if sak == 1:
            antal = antal + 1
        if sak == 2:
            antal2 = antal2 + 1
        if sak == 3:
            antal3 = antal3 + 1
        if sak == 4:
            antal4 = antal4 + 1
        if sak == 5:
            antal5 = antal5 + 1
        if sak == 6:
            antal6 = antal6 + 1
    svar = input("Vill du spela igen?")
