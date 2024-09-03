tal = int(input("Mata in ett hel tal"))
if tal <= 9 and tal >= 0:
    print (tal, "är ensiffrigt")
elif tal <= 99 and tal >= 10:
    print (tal, "är tvåsiffrigt")
elif tal <= 999 and tal >= 100:
    print(tal, "är tre siffrigt")
elif tal >= 1000:
    print(tal, "är minst fyrsiffrigt")
else: 
    print(tal, "är negativt")