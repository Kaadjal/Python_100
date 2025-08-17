def access():
  while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "LetsB00gie!":
        print("Welcome, ", username)
        break
    else:
        print("Incorrect username and/or password. Try again!")
        continue


print("Welcome to the Party!")
access()
