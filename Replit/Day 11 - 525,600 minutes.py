print("Find out the seconds in a year.")
year = int(input("What year is this for? "))

# A leap year is every 4 years, but not every 100 years, then again every 400 years.
if year % 400 == 0:
  time_sec = 366 * 24 * 60 * 60
  print("This is a leap year, so there are", time_sec, "seconds in this year.")
elif year % 4 == 0 and year % 100 != 0:
  time_sec = 366 * 24 * 60 * 60
  print("This is a leap year, so there are", time_sec, "seconds in this year.")
else:
  time_sec = 365 * 24 * 60 * 60
  print("This is not a leap year, so there are", time_sec, "seconds in this year.")

  
