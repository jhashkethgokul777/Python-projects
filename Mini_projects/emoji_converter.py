message = input(">")
words = message.split(' ')
emoji = {
      'funny' :  '😁',
      'sad' :  '😔',
      'love' : '😍',
      'lol' : '🤣',
      'welldone' : '👍'
      
 }
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)





    