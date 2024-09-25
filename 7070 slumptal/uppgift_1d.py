import random 
pengapung = 0
insattbelopp = 0
svar = 0
print("Välkommen att kasta tärning")
print("Ett spel kostar 1 krona")
print("Vinstplan:")
print("Två lika - 5 kr")
print("En sexa - 3 kr")
print("Stege - 3 kr")
while svar != "a":
    svar = input("Välj spel (s), Sätt in pengar (i), eller avsluta (a):")
    if svar == "i":
        insattbelopp = int(input("Ange belopp att sätta in"))
        pengapung = pengapung + insattbelopp
        print("Att spela för:", pengapung)
    elif svar == "s" and pengapung > 0:
        pengapung = pengapung - 1
        tal2 = random.randrange(1,7)
        print(tal2)
        tal1 = random.randrange(1,7)
        print(tal1)
        if tal1 + 1 == tal2 or tal2 + 1 == tal1:
            print("Steg-vinst + 3 kr")
            pengapung = pengapung + 3
            print("Att spela för:", pengapung)
        elif tal2 == 6 or tal1 == 6:
            print("Sex-vinst + 3 kr")
            pengapung = pengapung + 3
            print("Att spela för:", pengapung)
        elif tal2 == tal1:
            print("Vinst + 5 kr")
            pengapung = pengapung + 5
            print("Att spela för:", pengapung)
        else:
            print("Förlust")
            print("Att spela för:", pengapung) 
if svar == "a":
    print("Inga spel för dig,", pengapung, "i din pengapung")