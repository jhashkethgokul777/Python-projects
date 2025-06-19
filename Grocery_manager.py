Basket = []
print("Enter your groceries.")
while True:
  takes = input("Enter your items: ")
  if takes != 'remove':
    Basket.append(takes)
    print("Added: ",Basket)
  elif takes.upper() == 'REMOVE':
    removing = input("Enter to remove: ")
    Basket.remove(removing)
    print(f"Removing item {removing.upper()}")
    print("Updated basket:", Basket)
  elif takes.lower() == 'basket':
    print(Basket)

  
  

  
  

