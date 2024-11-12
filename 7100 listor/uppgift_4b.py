svar = ""
sak = "snopp"
alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö", ]
ord = input("dekryptera ord")
for bokstav in ord:
    if bokstav in alfa:
        if bokstav == alfa[0]:
            bokstav = alfa[28]
            svar += bokstav
        else:
            sak = alfa.index(bokstav)
            svar += alfa[sak - 1]
print(svar)