print("Hello There.This is a Guessing Game.")
print("You have Three chances..")
secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
   guess = int(input("Guess: "))
   guess_count += 1
   if guess == secret_number:
      print("WOW CONGRATS!YOU WON!")
      break
   elif guess > secret_number:
    print("Too high.Try Again.")
   elif guess < secret_number:
    print("Too low.Try Again")
else:
  print("No more Chances")
   
    
      