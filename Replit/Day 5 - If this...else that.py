animal = input("Are you an animal? ")
melt = input("Do you melt in the sun? ")
swim = input("Can you swim? ")
if animal == "no" and melt == "yes":
  print("you're olaf")
elif animal == "yes" and swim == "yes":
  print("you're flounder")
else:
  print("you're pumba")