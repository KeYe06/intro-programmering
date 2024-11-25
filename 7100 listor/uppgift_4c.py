svar = ""
sak = "snopp"
steg = 1
alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö", ]
ord = input("kryptera ord")
steg = int(input("hur många steg"))
for bokstav in ord:
    if bokstav in alfa:
        sak = alfa.index(bokstav)
        if sak > 28 - steg and bokstav != "ö":
            bokstav = alfa[0 + steg - (28 - sak) - 1] 
            svar += bokstav
        elif bokstav == "ö":
            bokstav = alfa[0 + steg - 1]
            svar += bokstav
        else:
            svar += alfa[sak + steg]
print(svar)