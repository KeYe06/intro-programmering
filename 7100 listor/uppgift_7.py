import random
#        0     1  2  3  4  5  6  7  8  9     10       11      12
deck = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "King", "Jester"]
deckx = ["Ace", "Ace", "Ace", "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "King", "Jester" "Queen", "King", "Jester" "Queen", "King", "Jester" "Queen", "King", "Jester"]
con = input("vill du spela black jack? j/n")
card = 0
cardcount = 49
while con != "n":
    sdeck = []
    sdecksum = []
    adeck = []
    adecksum = []
    adeckcheck = []
    for i in range (2):
        card = random.randint(0,cardcount)
        sdeck.append(deckx[card])
        deckx.pop(card)
        cardcount = cardcount - 1
    for i in range (2):
        card = random.randint(0,cardcount)
        adeck.append(deckx[card]) 
        deckx.pop(card)
        cardcount = cardcount - 1
    for i in adeck:
        if i == "Ace":
             adecksum.append(1)
             adeckcheck.append(1)
        elif i == "Queen" or i == "Jester" or i == "King":
             adecksum.append(10)
             adeckcheck.append(10)
        else:
             adecksum.append(i)
             adeckcheck.append(i)
    print("Ditt deck:", sdeck)
    svar = input("HIT ELLER STAND")
    while svar != "stand":
        card = random.randint(0,cardcount)
        sdeck.append(deckx[card]) 
        deckx.pop(card)
        cardcount = cardcount - 1
        print("Spelare: HIT")
        print("AI grumlar...")
        if sum(adecksum) <= 16:
            card = random.randint(0,cardcount)
            adeck.append(deckx[card])
            deckx.pop(card)
            cardcount = cardcount - 1
            for i in adeck:
                if i in adeckcheck:
                    adeckcheck.pop[i]
                if i == "Ace":
                    adecksum.append(1)
                    adeckcheck.append(1)
                elif i == "Queen" or i == "Jester" or i == "King":
                    adecksum.append(10)
                    adeckcheck.append(10)
                else:
                    adecksum.append(i)
                    adeckcheck.append(i)
            adeckscheck.extend(adecksum)
            print("AI: HIT")
        elif sum(adecksum) >= 16:
            print("AI: STAND")
        print("Ditt deck:", sdeck)
        svar = input("HIT ELLER STAND")
    while svar == "stand":
        print("AI grumlar...")
        if sum(adecksum) <= 16:
            card = random.randint(0,cardcount)
            adeck.append(deckx[card]) 
            deckx.pop(card)
            cardcount = cardcount - 1
            for i in adeck:
                if i in adeckcheck:
                    adeckcheck.pop(i)
                if i == "Ace":
                    adecksum.append(1)
                elif i == "Queen" or i == "Jester" or i == "King":
                    adecksum.append(10)
                else:
                    adecksum.append(i)
            adeckscheck.extend(adecksum)
            print("AI: HIT")
            svar = input("HIT ELLER STAND")
        elif sum(adecksum) >= 16:
            print("AI: STAND")
            for i in sdeck:
                if i == "Ace":
                    sdecksum.append(1)
                elif i == "Queen" or i == "Jester" or i == "King":
                    sdecksum.append(10)
                else:
                    sdecksum.append(i)
            if sum(sdecksum) > 21 and "Ace" in sdeck:
                sdecksum.pop[10]
                sdecksum.append(1)
            print("Spelarens deck:", sdeck)
            print("Din summa:", sum(sdecksum))
            print("AIs summa", sum(adeck))
            if sum(sdecksum) == 21:
                print("Black Jack för spelare")
            elif sum(adecksum) == 21:
                print("Black Jack för AI")
            elif sum(sdecksum) < sum(adecksum) and sum(adecksum) <= 21:
                print("AI vinner")
            elif sum(adecksum) < sum(sdecksum) and sum(sdecksum) <= 21:
                print("Spelare segrar")
            elif sum(sdecksum) > 21 and sum(adecksum) < 21:
                print("AI vinner")
            elif sum(adecksum) > 21 and sum(sdecksum) < 21:
                print("Spelare vinner")
            else:
                print("Lika")
            con = input("Stick härifrån")


