print("Welcome to the jokester!")
name = input(str("What is your name? "))
day = input(str("What day is it? "))
pick = input(str("Pick a song or a joke "))
mood = input(str("Positive or negative? "))  

print("Hello", name, "this is your personal message for today!")
if day.lower() == "monday": 
  if pick.lower() == "song" and mood.lower() == "positive":
    print("I hope you keep having a good day! I recommend 'Manic Monday' by The Bangles. You might have heard of it")
  elif pick.lower() == "song":
    print("I hope you will have a better day! I recommend 'I Don't Like Mondays' by the Boomtown Rats. It seems to fit your mood")
  else:
    print("How do cheeses greet each other on Monday mornings?")
    print()
    print("Have a Gouda week!")
    
if day.lower() == "tuesday": 
  if day.lower() == "tuesday" and mood.lower() == "positive":
    print("I hope you keep having a good day! I recommend 'Ruby Tuesday' by The Rolling Stones. It might seem familiar.")
  elif pick.lower() == "song":
    print("Second day of the week, have a good one! Here is a song for you: 'Tuesday's Gone' by Lynyrd Skynyrd")
  else:
    print("Why didn’t the French chef realize it was pancake Tuesday?")
    print()
    print("It Crêpe’d up on him.")

if day.lower() == "wednesday":
  if pick.lower() == "song" and mood.lower() == "positive":
    print("Midweek already, soon it will be weekend. I recommend 'Waiting for Wednesday' by Lisa Loeb. It will be a good day.")
  elif pick.lower() == "song":
    print("Halfway there, keep going! I recommend 'Wednesday Morning 3am' by Simon & Garfunkel. You might have heard of it.")
  else:
    print("What’s the worst part about Friday afternoons?")
    print()
    print("Realizing it’s just Wednesday.")

if day.lower() == "thursday":
  if pick.lower() == "song" and mood.lower() == "positive":
    print("Weekend is almost there. Here is your song for the day: 'Thursday' by Jess Glynne. Have a beautiful day!")
  elif pick.lower() == "song": 
    print("Almost there! I recommend 'Thursday's Child' by David Bowie. It will be a good day")
  else:
    print("The teacher asked why her student has been late 4 times this week… the student replied “because it’s only Thursday.”")

if day.lower() == "friday":
  if pick.lower() == "song" and mood.lower() == "positive":
    print("It's Friday! I recommend 'Friday I'm in Love' by The Cure. It will be a good day!")
  elif pick.lower() == "song":
    print(name, "it's Friday! I recommend 'Friday' by Rebecca Black. I hope you have a good day!")
    print()
    print("That was a joke, wasn't it? Your song is 'Last Friday Night TGIF' by Katy Perry.. Now doesn't that sound better?")
  else:
      print("What did the Iceberg say to the Romaine on Friday?")
      print()
      print("Lettuce celebrate!")

if day.lower() == "saturday":
  if pick.lower() == "song" and mood.lower() == "positive":
    print("Weekend.. Night Fever time.. that is also your song for today: 'Saturday Night Fever' by The BeeGees. Have a good one!")
  elif pick.lower() == "song":
    print("Kick it up to the next level! Your song for today is 'Someday I'll Be Saturday Night' by Bon Jovi. Have a great weekend!")
  else:
      print("Why did Han go shopping on Saturday?")
      print()
      print("Because the sale prices were Solo.")

if day.lower() == "sunday": 
  if pick.lower() == "song" and mood.lower() == "positive":
    print("Keep up the Sunday Funday mood. Listen to 'Sunday Morning Coming Down' by Johnny Cash. Sunday Funday!")
  elif pick.lower() == "song":
    print("Lazy Sunday..I recommend 'Lazy Sunday Afternoon' by The Small Faces. Hope you have one!")
  else:
    print("Why are Saturday and Sunday strong?")
    print()
    print("Because all the other days are week days.")

else: 
  print("Please select a day!")
print(name, "I hope this brightens yout day! Have a good one!")