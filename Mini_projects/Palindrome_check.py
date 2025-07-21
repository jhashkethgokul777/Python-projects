def palindrome(text):
  cleaned = ''.join(char.lower() for char in text if char.isalnum())
  return cleaned == cleaned[::-1]
  
  
word = input("Enter your text: ")
if palindrome(word):
  print("It’s a palindrome. ")
else:
  print("Not a palindrome.")