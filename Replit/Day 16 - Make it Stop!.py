print("Fill in the blanks to complete the lyrics!")

counter = 0
while True:
  lyric = input("Never going to ______ you up. ")
  if lyric.lower() == "give":
    print("Excellent!")
    break
  else:
    print("Nope, try again.")
    counter += 1
  if lyric.lower() == "give":
    break

print("Thanks for playing!")
print("Well done! It only took you", counter, "attempt(s).")
