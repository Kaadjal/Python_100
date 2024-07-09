course = input("Which course is this for? ")
max_score = int(input("What is the maximum number of points you could receive: "))
your_score = int(input("What is your score:  "))

percentage = round(your_score / max_score * 100, 2)
if percentage >= 90:
  letter_grade = "A+"
elif percentage >= 80:
  letter_grade = "A"
elif percentage >= 70:
  letter_grade = "B"
elif percentage >= 60:
  letter_grade = "C"
elif percentage >= 50:
  letter_grade = "D"
else:
  letter_grade = "U"

print("You got", percentage, "% for", course, "which is a(n)", "\033[34m", letter_grade)
