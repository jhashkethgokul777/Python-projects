import random
import string

def gen_password(length=6, upper_case=True, lower_case=True,symblos=True, numbers=True):
  characters = list(string.ascii_lowercase)
  characters += list(string.ascii_uppercase)
  characters += list(string.punctuation)
  characters += list(string.digits)
  password = ''.join(random.choices(characters, k=length))
  return password
  
if __name__ == "__main__":
  length = int(input("Enter your length: "))
  upper = input("Want uppercase(Y/N): ").lower() == 'y'
  lower = input("Want lowercase(Y/N): ").lower() == 'y'
  symbol = input("want symbols(Y/N): ").lower() == 'y'
  number = input("want numbers(Y/N): ").lower() == 'y'
  password = gen_password(length, upper, lower, number)
  print("Your generated password: ",password)
