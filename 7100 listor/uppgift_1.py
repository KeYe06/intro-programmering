import random
tärningar =[]
for i in range(10):
    tärningar.append(random.randint(1,6))
antal = [0, 0, 0, 0, 0, 0]
for tal in tärningar:
    if tal == 1:
        antal[0] = antal[0] + 1
    elif tal == 2:
        antal[1] = antal[1] + 1
    elif tal == 3:
        antal[2] = antal[2] + 1
    elif tal == 4:
        antal[3] = antal[3] + 1
    elif tal == 5:
        antal[4] = antal[4] + 1
    elif tal == 6:
        antal[5] = antal[5] + 1
tärningar.sort()
print(tärningar)
print("summa", sum(tärningar))
print("medelvärde", sum(tärningar) / len(tärningar))
print("min", min(tärningar))
print("max", max(tärningar))
print("antal", len(tärningar))
if antal[0] > antal[1] and antal[0] > antal[2] and antal[0] > antal[3] and antal[0] > antal[4] and antal[0] > antal[5]:
    print("finns mest ettor, antal ettor:", antal[0])
elif antal[1] > antal[0] and antal[1] > antal[2] and antal[1] > antal[3] and antal[1] > antal[4] and antal[1] > antal[5]:
    print("finns mest tvåor, antal tvåor:", antal[1])
elif antal[2] > antal[0] and antal[2] > antal[1] and antal[2] > antal[3] and antal[2] > antal[4] and antal[2] > antal[5]:
    print("finns mest treor, antal treor:", antal[2])
elif antal[3] > antal[0] and antal[3] > antal[1] and antal[3] > antal[2] and antal[3] > antal[4] and antal[3] > antal[5]:
    print("finns mest fyror, antal fyror:", antal[3])
elif antal[4] > antal[0] and antal[4] > antal[1] and antal[4] > antal[2] and antal[4] > antal[3] and antal[4] > antal[5]:
    print("finns mest femmor, antal femmor:", antal[4])
elif antal[5] > antal[0] and antal[5] > antal[1] and antal[5] > antal[2] and antal[5] > antal[3] and antal[1] > antal[4]:
    print("finns mest sexor, antal sexor:", antal[1])
else:
    print("mer än ett tal har mest")