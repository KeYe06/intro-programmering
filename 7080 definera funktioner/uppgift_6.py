def truorfal(tal):
    if tal % 2 == 0:
        return "true"
    else:
        return "false"
tal = int(input("Ange ett tal"))
print(truorfal(tal))