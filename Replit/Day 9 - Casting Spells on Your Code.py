name = input("What is your name? ")
year = int(input("What year were you born? "))

if year >= 1925 and year <= 1946:
  print(name, "You're a traditionalist! \U0001F614")
elif year >= 1947 and year <= 1964:
  print(name, "You're a baby boomer! Thanks for the economy! \U0001F923")
elif year >=1965 and year <= 1981:
  print(name, "You're a Gen X! \U0001F921")
elif year >= 1982 and year <= 1995:
  print(name, "Millenial what's up! \U0001F612")
elif year >= 1996 and year <= 2015:
  print(name, "You're a Gen Z! Get of TikTok! \U0001F913")
elif year >= 2016 and year <= 2023:
  print(name, "You're a Gen Alpha! Get of the internet! ")
else:
  print("You're either too old or too young to be on this website!")
