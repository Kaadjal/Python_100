from getpass import getpass as input
print("E P I C    🪨  📄 ✂️  \U0001F98E \U0001F596  B A T T L E")
print()
print("Welcome to the game of Rock, Paper, Scissors, Lizard, Spock!")
print()
print("Here are the rules for those who are new: ")
print("""Scissors cuts paper,
paper covers rock,
rock crushes Lizard,
Lizard poisons Spock,
Spock smashes scissors,
scissors decapitates Lizard,
Lizard eats paper,
paper disproves Spock,
Spock vaperizes rock,
and as it always has,
rock crushes scissors.
""")
print()
print("Each player will make a selection of either Rock, Paper, Scissors, Lizard, or Spock.")
print("Select your move as (R, P, S, L or Sp)")
print()

score1 = 0
score2 = 0

while True:
  player1 = input("Player 1:  ").lower()
  print()
  player2 = input("Player 2:  ").lower()
  print()

  if player1 == player2:
    print("Both players selected:", player1)
    print("It's a tie!")
    score1 = score1
    score2 = score2
  elif player1 == "r" and (player2 == "s" or player2 == "l"):
    print("Player 1 selected:", player1, "and Player 2 selected:", player2)
    print("Rock Smashes! 🪨")
    print("Player 1 wins!")
    score1 += 1
    score2 = score2
  elif player1 == "p" and (player2 == "r" or player2 == "sp"):
    print("Player 1 selected:", player1, "and Player 2 selected:", player2)
    print("Darn those Paper cuts! 📄")
    print("Player 1 wins!")
    score1 += 1
    score2 = score2
  elif player1 == "s" and (player2 == "p" or player2 == "l"):
    print("Player 1 selected:", player1, "and Player 2 selected:", player2)
    print("Chop, chop, chop from Scissors! ✂️")
    print("Player 1 wins!")
    score1 += 1
    score2 = score2
  elif player1 == "l" and (player2 == "sp" or player2 == "p"):
    print("Player 1 selected:", player1, "and Player 2 selected:", player2)
    print("Watch out for poison from the Lizard! \U0001F98E")
    print("Player 1 wins!")
    score1 += 1
    score2 = score2
  elif player1 == "sp" and (player2 == "r" or player2 == "s"):
    print("Player 1 selected:", player1, "and Player 2 selected:", player2)
    print("Live long and prosper from Spock! \U0001F596")
    print("Player 1 wins!")
    score1 += 1
    score2 = score2
  else:
    print("Player 1 selected:", player1, "and Player 2 selected:", player2)
    print("Player 2 wins! \U0001F973")
    score1 = score1
    score2 += 1

  print("Player 1 has", score1, "points and Player 2 has", score2, "points.")

  if score1 == 3 or score2== 3:
    print("Thanks for playing!")
    exit()
  else:
    continue
