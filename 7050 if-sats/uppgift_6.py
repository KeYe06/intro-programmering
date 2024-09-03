tal = float(input("Mata in ett tal"))
tal2 = float(input("Mata in ett till tal"))
tal3 = float(input("Mata in ännu ett tal"))
if tal < tal2 and tal2 < tal3:
    print(tal, tal2, tal3)
elif tal2 < tal and tal < tal3:
    print(tal2, tal, tal3)
elif tal3 < tal and tal < tal2:
    print(tal3, tal, tal2)
elif tal < tal3 and tal3 < tal2:
    print(tal, tal3, tal2)
elif tal2 < tal3 and tal3 < tal:
    print(tal2, tal3, tal)
elif tal3 < tal2 and tal2 < tal:
    print(tal3, tal2, tal)



