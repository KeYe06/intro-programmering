tal = int(input("mata in ett tal"))
if tal >= 0 and tal <= 9:
    print("talet är ensiffrigt")
elif tal <= 99 and tal >= 10:
    print("talet är tvåsiffrigt")
elif tal <= 999 and tal >= 100:
    print("talet är tresiffrigt")
elif tal >= 1000:
    print("talet är minst fyrsiffrigt")
else:
    print("talet är negativt")