tal = int(input("Mata in ett hel tal:"))
tal2 = int(input("Mata in ett till hel tal:"))
tal3 = int(input("Mata in ännu ett till hel tal:"))
if tal < tal2 and tal < tal3:
    print (tal, "är minst av de tal som du skrev")
elif tal2 < tal and tal2 < tal3:
    print (tal2, "är minst av de tal som du skrev")
elif tal3 < tal and tal3 < tal3:
    print (tal3, "är minst av de tal som du skrev")
else:
    print("alla tal är lika")