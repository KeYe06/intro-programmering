månad = input("Vilken månad fyller du år?")
if månad == "januari" or månad == "Januari" or månad =="Februari" or månad =="februari" or månad =="December" or månad =="december":
    print("Du är född i vintern")
elif månad == "mars" or månad =="Mars" or månad =="April" or månad =="april" or månad =="Maj" or månad =="maj":
    print("Du är född i våren")
elif månad == "Juni" or månad =="juni" or månad =="Juli" or månad =="juli" or månad =="Augusti" or månad =="augusti":
    print("Du är född i sommaren")
elif månad == "September" or månad =="september" or månad =="Oktober" or månad =="oktober" or månad =="November" or månad =="november":
    print("Du är född i hösten")
else:
    print("FEL!")