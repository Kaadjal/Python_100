APR=0.05
loan = 1000.00
for i in range(10):
  loan += APR*loan
  print("Year", i+1, "is", round(loan,2))
