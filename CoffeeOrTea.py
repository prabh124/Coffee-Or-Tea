def displayMenu(name):
    print("Hi,", name + "! Would you like coffee or tea?")
    beverageType = input()
    beverageType = beverageType.lower()

    if (beverageType == ("tea") or beverageType == ("t")):
        return 'tea'
    elif (beverageType == ("coffee") or beverageType == ("c")):
        return 'coffee'
    else:
        print("ERROR: Invalid input!")
        exit()
    

def sizeOfBeverage(beverage):
    print("What sized", beverage, "would you like?")
    size = input()
    size = size.lower()

    if (size == 's') or (size == 'small'):
        return 'small', 1.50
    elif (size == 'm') or (size == 'medium'):
        return 'medium', 2.50
    elif (size == 'l') or (size == 'large'):
        return 'large', 3.25
    else:
        print("ERROR: Invalid input!")
        exit()

def teaFlavour(beverage):
    print("What flavour", beverage, "would you like? (None, Lemon, or Mint)")
    flavour = input()
    flavour = flavour.lower()

    if (flavour == '') or (flavour == 'none'):
        return 'no Flavouring', 0.0
    elif (flavour == 'l') or (flavour == 'lemon'):
        return 'lemon', 0.25
    elif (flavour == 'm') or (flavour == 'medium'):
        return 'mint', 0.5
    else:
        print("ERROR: Invalid input!")
        exit()

def coffeeFlavour(beverage):
    print("What flavour", beverage, "would you like? (None, Chocolate, or Vanilla)")
    flavour = input()
    flavour = flavour.lower()

    if (flavour == '') or (flavour == 'none'):
        return 'no flavouring', 0.0
    elif (flavour == 'c') or (flavour == 'chocolate'):
        return 'vhocolate', 0.75
    elif (flavour == 'v') or (flavour == 'vanilla'):
        return 'vanilla', 0.25
    else:
        print("ERROR: Invalid input!")
        exit()



while True:
    name = input("What is your name?\n")
    if ' ' in name:
        print("ERROR: Invalid input!")
        break
    cost = 0
    temp = 0
    flavour = ''
    beverage = displayMenu(name)

    size, temp = sizeOfBeverage(beverage)
    cost += temp

    if (beverage == 'tea'):
        flavour, temp = teaFlavour(beverage)
    else:
        flavour, temp = coffeeFlavour(beverage)
    cost += temp
    
    cost *= 1.13
    cost = round(cost, 2)

    print("For", name + ", a", size, beverage + ",", flavour, "cost: $" + str(cost))
    break

 

