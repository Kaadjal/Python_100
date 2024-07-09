movie = input("What is your favorite movie? ")
if movie == "Harry Potter":
  print("Cool, a fellow potterhead")
  char = input("Who is your favorite character? ")
  if char == "Monagal":
    print("Yeah she is badass!")
  elif char == "Neville":
    print("Yeah he is a good guy!")
  else:
    print("Oh, okay")
elif movie == "Star Wars":
  print("Cool which trilogy?")
  trilogy = input("Which trilogy? ")
  if trilogy == "Original":
    print("Same dude, same")
  elif trilogy == "prequel":
    print("Those are not too bad")
  else:
    print("Why?")
else:
  print("it seems we like different things")
  