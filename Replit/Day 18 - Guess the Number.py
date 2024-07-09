import random

num_to_guess = random.randint(1, 1000)

count = 0
while True:
  user_guess = int(input("What number between 1 and 1000 do you guess? "))
  if user_guess > num_to_guess:
    print("The number you guessed should be lower")
    if abs(user_guess - num_to_guess) <= 20:
      print("You are quite close though")
    elif abs(user_guess - num_to_guess) <= 100:
      print("You are a bit off")
    else:
      print("You're quite far off!")
    count += 1
  elif user_guess < num_to_guess:
    print("Your guess should be higher")
    if abs(user_guess - num_to_guess) <= 20:
      print("Very close though")
    elif abs(user_guess - num_to_guess) <= 100:
      print("A bit off")
    else:
      print("So far away!")
    count += 1
  elif user_guess == num_to_guess:
    print("Brilliant!!! You got it! The number was", num_to_guess)
    count += 1
    break
  else:
    print("Number unknown")

print("It took you", count, "guess(es) to guess the number.")
