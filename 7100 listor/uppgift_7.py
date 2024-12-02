import random
#        0     1  2  3  4  5  6  7  8  9     10       11      12
deck = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "King", "Jester"]
con = input("vill du spela black jack? j/n")
while con != "n":
    sdeck = []
    sdecksum = []
    adeck = []
    adecksum = []
    for i in range (2):
        sdeck.append(deck[random.randint(0, 12)])
    for i in range (2):
        adeck.append(deck[random.randint(0, 12)])
    print("Ditt deck:", sdeck)
    svar = input("HIT ELLER STAND")
    while svar != "stand":
        sdeck.append(deck[random.randint(0,12)])
        print("Spelare: HIT")
        print("Ditt deck:", sdeck)
        print("AI grumlar...")
        if sum(adecksum) <= 16:
            adeck.append(deck[random.randint(0,12)])
            print("AI: HIT")
        elif sum(adeck) >= 16:
            print("AI: STAND")
        svar = input("HIT ELLER STAND")
    while svar == "stand":
        print("AI grumlar...")
        if sum(adecksum) <= 16:
            adeck.append(deck[random.randint(0,12)])
            print("AI: HIT")
            svar = input("HIT ELLER STAND")
        elif sum(adeck) >= 16:
            print("AI: STAND")
            for burger in adeck:
                if burger == "Ace":
                    adecksum.append(1)
                elif burger == "Queen" or burger == "king" or burger == "Jester":
                    adecksum.append(10)
                else:
                    adecksum.append(burger)
            for burger in sdeck:
                if burger == "Ace":
                    sdecksum.append(1)
                elif burger == "Queen" or burger == "king" or burger == "Jester":
                    sdecksum.append(10)
                else:
                    sdecksum.append(burger)
            print("Spelarens deck:", sdeck)
            print("Din summa:", sum(sdecksum))
            print("AIs deck:", adeck)
            print("AIs summa", sum(adecksum))
            if sum(sdecksum) == 21:
                print("Black Jack för spelare")
            elif sum(adecksum) == 21:
                print("Black Jack för AI")
            elif sum(sdecksum) < sum(adecksum) and sum(adecksum) <= 21:
                print("AI vinner")
            elif sum(adecksum) < sum(sdecksum) and sum(sdecksum) <= 21:
                print("Spelare segrar")


