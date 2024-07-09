food = input("What food is the base? ")
plant = input("What plant will you add? ")
cook = input("How will we cook this food? ")
burn = input("How will we describe burned food? ")
household_item = input("Think of a household item: ")
color = input("What is your favourite color? ")
fruit = input("Name a fruit ")
toy = input("What is your favourite toy? ")
booze = input("What is your poison? ")
flower = input("Name a flower")

dinner = f"{cook} {food} with {burn} {plant} on a bed of {household_item} served on a {color} plate"
desert = f"{fruit} served in {toy}"
drink = f"{booze} served in a {color} glass, garnished with {flower}"
print()
print("Menu")
print(dinner)
print(desert)
print(drink)
