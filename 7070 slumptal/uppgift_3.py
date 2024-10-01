import random
svar = 0
svar = input("Vill du spela sten, sax, påse? y/n")
while svar != "n":
    val = input("Sten, sax eller påse")
    tal = random.randrange(1,4)
    if val == "sten" and tal == 1:
        print("(DU)\STEN vs STEN/(DATOR) --- Ingen segrare")
    elif val == "sax" and tal == 1:
        print("(DU)\SAX vs STEN/(DATOR) --- DATOR segrar")
    elif val == "sten" and tal == 1:
        print("(DU)\PÅSE vs STEN/(DATOR) --- SPELARE segrar")
    elif val == "sax" and tal == 2:
        print("(DU)\SAX vs SAX/(DATOR) --- Ingen segrare")
    elif val == "sten" and tal == 2:
        print("(DU)\STEN vs SAX/(DATOR) --- SPELARE segrar")
    elif val == "påse" and tal == 2:
        print("(DU)\PÅSE vs SAX/(DATOR) --- DATOR segrar")
    elif val == "påse" and tal == 3:
        print("(DU)\PÅSE vs PÅSE/(DATOR) --- Ingen segrare")
    elif val == "sten" and tal == 3:
        print("(DU)\STEN vs PÅSE/(DATOR) --- DATOR segrar")
    elif val == "sax" and tal == 3:
        print("(DU)\SAX vs PÅSE/(DATOR) --- SPELARE segrar")
    else:
        print("Skriv något vettigt")
    svar = input("Spela igen? y/n")
print("Inga mer spel")

