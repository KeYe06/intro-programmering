import random
pointspelare = 0
pointai = 0
rundor = 0
svar = input("Vill du köra sten sax påse? y/n")
while svar != "n":
    val = input("Välj sten, sax eller påse")
    ai = random.randrange(1,4)
    if val == "sten" and ai == 1:
        rundor = rundor + 1
        print("Spelare:", pointspelare)
        print("AI:", pointai)
        svar = input("SPELARE - STEN vs STEN - AI ... lika, vill du spela igen? y/n")
    elif val == "sten" and ai == 2:
        rundor = rundor + 1
        pointspelare = pointspelare + 1
        print("Spelare:", pointspelare)
        print("AI:", pointai)
        svar = input("SPELARE - STEN vs SAX - AI ... vinst, vill du spela igen? y/n")
    elif val == "sten" and ai == 3:
        rundor = rundor + 1
        pointai = pointai + 1
        print("Spelare:", pointspelare)
        print("AI:", pointai)
        svar = input("SPELARE - STEN vs PÅSE - AI ... förlust, vill du spela igen? y/n")
    elif val == "sax" and ai == 1:
        rundor = rundor + 1
        pointai = pointai + 1
        print("Spelare:", pointspelare)
        print("AI:", pointai)
        svar = input("SPELARE - SAX vs STEN - AI ... förlust, vill du spela igen? y/n")
    elif val == "sax" and ai == 2:
        rundor = rundor + 1
        print("Spelare:", pointspelare)
        print("AI:", pointai)
        svar = input("SPELARE - SAX vs SAX - AI ... lika, vill du spela igen? y/n")
    elif val == "sax" and ai == 3:
        rundor = rundor + 1
        pointspelare = pointspelare + 1
        print("Spelare:", pointspelare)
        print("AI:", pointai)
        svar = input("SPELARE - SAX vs PÅSE - AI ... vinst, vill du spela igen? y/n")
    elif val == "påse" and ai == 1:
        rundor = rundor + 1
        pointspelare = pointspelare + 1
        print("Spelare:", pointspelare)
        print("AI:", pointai)
        svar = input("SPELARE - PÅSE vs STEN - AI ... vinst, vill du spela igen? y/n")
    elif val == "påse" and ai == 2:
        rundor = rundor + 1
        pointai = pointai + 1
        print("Spelare:", pointspelare)
        print("AI:", pointai)
        svar = input("SPELARE - PÅSE vs SAX - AI ... förlust, vill du spela igen? y/n")
    elif val == "påse" and ai == 3:
        rundor = rundor + 1
        print("Spelare:", pointspelare)
        print("AI:", pointai)
        svar = input("SPELARE - PÅSE vs PÅSE - AI ... lika, vill du spela igen? y/n")
if pointspelare > pointai:
    print(rundor, "rundor ... SPELARE:", pointspelare, "poäng --- AI:", pointai, "poäng .... SPELARE SEGRAR")
elif pointspelare < pointai:
    print(rundor, "rundor ... SPELARE:", pointspelare, "poäng --- AI:", pointai, "poäng .... AI SEGRAR")
else:
    print(rundor, "rundor ... SPELARE:", pointspelare, "poäng --- AI:", pointai, "poäng .... INGEN SEGRAR")
    