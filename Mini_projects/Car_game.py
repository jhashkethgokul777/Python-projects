enter = ""
started = False
while enter != 'quit':
  enter = input(">")
  if enter.upper() == 'START':
    if started:
      print("car already started to go")
    else:
      started = True
      print("car started to go.")
  elif enter.upper() == 'STOP':
    if not started:
      print("car is already  stopped")
    else:
      started = False
      print("Car is stopped..")
  elif enter.lower() == 'help':
    print('''
START-car starts to go 
STOP-car stops
QUIT-to exit''')
  elif enter.upper() == 'QUIT':
    print("ok.Thanks for playing")
    break
  else:
    print("I don't understand")
    
    
  