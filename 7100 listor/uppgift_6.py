alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö", ]
con = input("kryptera eller dekryptera? k/d")
if con == "k":
    svar = ""
    ord = input("läs in ett ord")
    for bokstav in ord:
        if bokstav in alfa:
            bokstav = alfa[28 - alfa.index(bokstav)]
            svar += bokstav
if con == "d":
    svar = ""
    ord = input("läs in ett ord")
    for bokstav in ord:
        if bokstav in alfa:
            bokstav = alfa[28 - alfa.index(bokstav)]
            svar += bokstav
print(svar)
