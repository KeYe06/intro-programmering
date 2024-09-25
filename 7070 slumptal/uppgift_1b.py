import random 
svar = input("Vill du spela? y/n")
while svar == "y":
    tal2 = random.randrange(1,7)
    print(tal2)
    tal1 = random.randrange(1,7)
    print(tal1)
    if tal2 == 6 and tal1 == 6:
        svar = input("Sex-vinst! Vill du spela igen? y/n")
    elif tal2 == tal1:
        svar = input("Vinst! Vill du spela igen? y/n")
    else:
        svar = input("Förlust! Vill du spela igen? y/n")
if svar == "n":
        print("Inga spel för dig")