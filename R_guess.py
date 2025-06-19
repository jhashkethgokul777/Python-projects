import random

secret_number = random.randint(1, 10)
count_num = 0
count_limit = 3

#Game Intrusctions...
print("Instructions: ")
print("This is a guessing game ")
print("You Need guess the number")
print("You Have Three Chances.")


while count_num < count_limit:
  Guess = int(input("Enter Guess: "))
  count_num += 1
  if secret_number == Guess:
    print("Wow,You Won..")
    break 
  elif secret_number > Guess:
    print("Low.")
  elif secret_number < Guess:
    print("High.")
else:
  print("\nNo More Chances..")