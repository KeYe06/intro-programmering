alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö", ]
def caesark(ord):
    svar = ""
    for bokstav in ord:
        sak = alfa.index(bokstav)
        bokstav = alfa[0 + steg - (28 - sak) - 1]
        svar += bokstav
    return svar
def caesard(ord):
    svar = ""
    for bokstav in ord:
        sak = alfa.index(bokstav)
        if sak - steg < 0:
            svar += alfa[len(alfa) - steg]
        else:
            svar += alfa[sak - steg]
    return svar
choice = input("Vill du dekryptera eller kryptera? d/k")
steg = int(input("Hur många steg?"))
ord = input("Ange ditt ord")
if choice == "k":
    print(caesark(ord))
if choice == "d":
    print(caesard(ord))


