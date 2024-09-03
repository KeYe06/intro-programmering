tal1 = int(input("Mata in ett hel tal:"))
tal2 = int(input("Mata in ett annat tal:"))
if tal1 > tal2:
    print(tal1, "är större än", tal2)
elif tal1 == tal2:
    print("Talen är lika")
else:
    print(tal2, "är större än", tal1)