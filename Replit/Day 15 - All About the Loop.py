print("Welcome to fun with animal sounds!")
print()
print("Pick the animal you want to hear the sound of.")

exit = ""
animal = ""
while exit != "yes":
  animal = input("What animal do you want to hear? ")
  if animal == "dog":
    print("woof.. woof.. did someone bring moon moon?")
  elif animal == "cat":
    print("le meow.. this is a very fancy French cat")
  elif animal == "cow":
    print("moooo the cow jumps over the moon")
  elif animal == "tiger":
    print("rooooooooaaaaaaaaar do you see who is the boss!?")
  elif animal == "pig":
    print("Oink, oink, oink, please don't eat me.. bacon bad!")
  elif animal == "parrot":
    print("Do you seriously need me to repeat you?")
    exit = input("Do you want to exit? ")
  elif animal == "sheep":
    print("Meeeh, don't be a sheep!")
  elif animal == "horse":
    print("Neigh neigh .. what did you expect?")
  elif animal == "chicken":
    print("tok tok tokkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk.. not TikTok")
  elif animal == "fish":
    print("blub blub blub.. what did you expect?")
  else:
    print("animal unknown, please select a different animal or exit")

  exit = input("Do you want to exit? ")
