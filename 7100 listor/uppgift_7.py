import random
import time
deckx = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "King", "Jack",]
con = input("Vill du spela black jack? j/n")
card = 0
cardcount = 12
while con != "n":
    print("Det finns 13 kort i kortleken")
    time.sleep(1.4)
    print("Ett av varje")
    time.sleep(1)
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
    time.sleep(1)
    print("AI har", len(adeck), "kort")
    print("AI har en/ett", adeck[0])
    time.sleep(1)
    svar = input("HIT ELLER STAND")
    while svar != "stand":
        card = random.randint(0,cardcount)
        sdeck.append(deckx[card]) 
        deckx.pop(card)
        cardcount = cardcount - 1
        print("Spelare: HIT")
        time.sleep(0.8)
        print("AI grumlar...")
        time.sleep(0.5)
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
        time.sleep(0.5)
        print("Ditt deck:", sdeck)
        time.sleep(1)
        print("AI har", len(adeck), "kort")
        print("AI har en/ett", adeck[0])
        time.sleep(1)
        svar = input("HIT ELLER STAND")
    while svar == "stand":
        print("Spelare: STAND")
        time.sleep(0.8)
        print("AI grumlar...")
        time.sleep(0.5)
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
            time.sleep(1)
            print("Ditt deck:", sdeck)
            time.sleep(1)
            print("AI har", len(adeck), "kort")
            print("AI har en/ett", adeck[0])
            time.sleep(1)
            svar = input("HIT ELLER STAND")
        elif sum(adecksum) >= 16:
            print("AI: STAND")
            for i in sdeck:
                if i == "Queen" or i == "Jack" or i == "King" or i == "Ace":
                    sdecksum.append(10)
                else:
                    sdecksum.append(i)
            time.sleep(0.8)
            if sum(sdecksum) > 21 and "Ace" in sdeck:
                final = sdeck.index("Ace")
                sdecksum.pop(final)
                sdecksum.append(1)    
                print("Spelares Ace omvandlas till en etta!")
            if sum(adecksum) > 21 and "Ace" in adeck:
                final = adeck.index("Ace")
                adecksum.pop(final)
                adecksum.append(1)
                print("AIs Ace omvandlas till en etta!")
            time.sleep(0.5)
            print("Spelarens deck:", sdeck)
            time.sleep(0.5)
            print("Din summa:", sum(sdecksum))
            time.sleep(0.5)
            print("AIs deck", adeck)
            time.sleep(0.5)
            print("AIs summa", sum(adecksum))
            time.sleep(1)
            if sum(sdecksum) == 21:
                print("Black Jack för spelare")
            elif sum(adecksum) == 21:
                print("Black Jack för AI")
            if sum(sdecksum) < sum(adecksum) and sum(adecksum) < 22:
                print("AI vinner")
            elif sum(adecksum) < sum(sdecksum) and sum(sdecksum) < 22:
                print("Spelare segrar")
            elif sum(sdecksum) > 22 and sum(adecksum) < 22:
                print("AI vinner")
            elif sum(adecksum) > 22 and sum(sdecksum) < 22:
                print("Spelare vinner")
            else:
                print("AI vinner")
            con = input("Stick härifrån")
if con == "n":
    print("Stick härifrån")