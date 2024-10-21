import random
svar = 0
pengapung = 3
while svar != "n" and pengapung > 0:
    print("Du har", pengapung,  "kr")
    svar = input("Skriv j för att spela och n för att sluta spela. Ett spel kostar 1 kr")
    if svar == "j":
         tal1 = random.randrange(10)
         print(tal1)
         tal2 = random.randrange(10)
         print(tal2)
         tal3 = random.randrange(10)
         print(tal3)
         pengapung = pengapung - 1
         if tal1 == tal2 and tal2 == tal3:
            print("STOR Vinst + 50 kr!!")
         elif tal1 == 7 and tal2 == tal1 and tal3 == tal1:
            pengapung = pengapung + 50
            print("JACKPOT 777 + 1000000 kr!!!!!!!!!!!!!!!!!!!!!!!")
            pengapung = pengapung + 1000000
         elif tal1 == tal2 or tal2 == tal3 or tal1 == tal3:
            print("Minivinst + 5 kr")
            pengapung = pengapung + 5
         elif tal1 == 7 or tal2 == 7 or tal3 == 7:
            print("Sjuvinst + 2 kr")
            pengapung = pengapung + 2
         else:
            print("FÖRLUST, SPELA IGEN! SPELA IGEN! SPELA IGEN! SPELA IGEN! SPELA IGEN!")
if svar == "n":
    print("Kom igen imorgon")
if pengapung == 0:
    print("PANK! Kom tillbaka med mer pengar!")