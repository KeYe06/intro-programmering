import random
deckx = ["Ace", "Ace", "Ace", "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "King", "Jack", "Queen", "King", "Jack", "Queen", "King", "Jack", "Queen", "King", "Jack"]
con = input("Vill du spela black jack? j/n")
card = 0
cardcount = 53
while con != "n":
    sdeck = []
    sdecksum = []
    adeck = []
    adecksum = []
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
        if i == "Queen" or i == "Jack" or i == "King" or i == "Ace":
             adecksum.append(10)
        else:
             adecksum.append(i)
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
            if adeck[-1] == "Queen" or adeck[-1] == "King" or adeck[-1] == "Jack" or adeck[-1] == "Ace":
                adecksum.append(10)
            else:
                adecksum.append(adeck[-1])
            print("AI: HIT")
        elif sum(adecksum) >= 16:
            print("AI: STAND")
        print("Ditt deck:", sdeck)
        svar = input("HIT ELLER STAND")
    while svar == "stand":
        print("Spelare: STAND")
        print("AI grumlar...")
        if sum(adecksum) <= 16:
            card = random.randint(0,cardcount)
            adeck.append(deckx[card]) 
            deckx.pop(card)
            cardcount = cardcount - 1
            for i in adeck:
                if adeck[-1] == "Queen" or adeck[-1] == "King" or adeck[-1] == "Jack" or adeck[-1] == "Ace":
                    adecksum.append(10)
                else:
                    adecksum.append(adeck[-1])
            print("AI: HIT")
            svar = input("HIT ELLER STAND")
        elif sum(adecksum) >= 16:
            print("AI: STAND")
            for i in sdeck:
                if i == "Queen" or i == "Jack" or i == "King" or i == "Ace":
                    sdecksum.append(10)
                else:
                    sdecksum.append(i)
            if sum(sdecksum) > 21 and "Ace" in sdeck:
                sdecksum.pop[10]
                sdecksum.append(1)    
            if sum(adecksum) > 21 and "Ace" in adeck:
                sdecksum.pop[10]
                sdecksum.append(1)
            print("Spelarens deck:", sdeck)
            print("Din summa:", sum(sdecksum))
            print("AIs summa", sum(adecksum))
            if sum(sdecksum) == 21:
                print("Black Jack för spelare")
            elif sum(adecksum) == 21:
                print("Black Jack för AI")
            if sum(sdecksum) < sum(adecksum) and sum(adecksum) <= 21:
                print("AI vinner")
            elif sum(adecksum) < sum(sdecksum) and sum(sdecksum) <= 21:
                print("Spelare segrar")
            elif sum(sdecksum) > 21 and sum(adecksum) < 21:
                print("AI vinner")
            elif sum(adecksum) > 21 and sum(sdecksum) < 21:
                print("Spelare vinner")
            else:
                print("AI vinner")
            con = input("Stick härifrån")
if con == "n":
    print("Stick härifrån")

