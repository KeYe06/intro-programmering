import random
svar = input("Vill du köra sten sax påse? y/n")
while svar != "n":
    val = input("Välj sten, sax eller påse")
    ai = random.randrange(1,4)
    if val == "sten" and ai == 1:
        svar = input("uied, vill du spela igen? y/n")
    