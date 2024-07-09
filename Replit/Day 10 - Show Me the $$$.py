myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = input("What percentage of tip would you like to leave? ")
amount = myBill * (1 + (int(tip)/100))
answer = round((amount/numberOfPeople),2)


print("You all owe", answer)
