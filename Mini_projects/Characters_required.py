username = input("Enter username: ")
if len(username) < 4:
  print("characters are less than 4")
elif len(username) > 12:
  print("characters are more than 12")
else:
  print("Access Granted")
