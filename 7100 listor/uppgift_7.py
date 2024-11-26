import random
#        0      1    2    3    4    5    6    7    8    9     10       11      12
deck = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Queen", "King", "Jester"]
sdeck = []
adeck = []
con = input("vill du spela black jack? j/n")
while con != "n":
    for i in range (2):
        sdeck.append(deck[random.randint(0,12)])
    for i in range (2):
        adeck.append(deck[random.randint(0, 12)])
    print("Ditt deck:", sdeck)
    svar = input("HIT ELLER STAND")
    while svar == "hit":
        sdeck.append(deck[random.randint(0,12)])
        print("Ditt deck:", sdeck)
        print("AI grumlar...")
        if sum(adeck) <= 16:
            adeck.append(deck[random.randint(0,12)])
        svar = input("HIT ELLER STAND")
    if svar == "stand":
        print("Spelarens deck:", sdeck)
        print("AIs deck:", adeck)
