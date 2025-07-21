weight = int(input("Enter weight: "))
units = input("kg(k) or lb(l)")
if units.upper() == 'K':
  converter = weight*2.205
  print(f" your weight is {converter} in pounds")
else:
  converter = weight/2.205
  print(f" your weight is {converter} in kilograms.")
