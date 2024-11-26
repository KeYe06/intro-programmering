import random
tärningar = []
a = [6, 6, 6, 6, 6]
b = [5, 5, 5, 5, 5]
c = [4, 4, 4, 4, 4]
d = [3, 3, 3, 3, 3]
e = [2, 2, 2, 2, 2]
f = [1, 1, 1, 1, 1]
svar = input("Vill du spela?")
while svar != "nej":
    for i in range (5):
        tärningar.append(random.randint(1, 6))
    if tärningar == a or tärningar == b or tärningar == c or tärningar == d or tärningar == e or tärningar == f:
        print("YATZYE")
        print(tärningar)
        tärningar = []
        svar = input("Vill du spela igen")
    else:
        print("NO YATSE")
        print(tärningar)
        tärningar = []
        svar = input("Vill du spela igen?")
