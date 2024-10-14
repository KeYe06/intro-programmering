tal = int(input("mata in ett tal"))
tal2 = int(input("mata in ett till tal"))
if tal < tal2:
    print(tal, "är mindre än", tal2)
elif tal2 < tal:
    print(tal2, "är mindre än", tal)
else:
    print("Talen är lika")