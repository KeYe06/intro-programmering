alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö", ]
sak = "snopp"
svar = ""
steg = 1
ord = input("dekryptera ord")
for bokstav in ord:
        if bokstav in alfa:
            sak = alfa.index(bokstav)
            if sak - steg < 0:
                svar += alfa[28 - steg + 1]
            else:
                svar += alfa[sak - steg]
con = input("Är ordet dekrypterat?", svar)
while con != "ja":
    for bokstav in ord:
        if bokstav in alfa:
            sak = alfa.index(bokstav)
            if sak - steg < 0:
                svar += alfa[28 - steg + 1]
            else:
                svar += alfa[sak - steg]
            con = input("Är ordet dekrypterat?", svar)