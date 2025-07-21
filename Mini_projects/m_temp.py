#Temp converter..

'''Features:

Converts between all three units: Celsius, Kelvin, Fahrenheit

Allows both uppercase and lowercase inputs (C/K/F)

Graceful error handling

Accurate formulas with decimal precision'''



print("This a temperature converter ")
print("Enter q to exit.")

while True:
  user_input = input("Enter your temp: ")
  if user_input.lower() == 'q':
    break
  try:
    temp = float(user_input)
    from_in = input("Enter from(C/K/F): ").lower()
    to_in = input("Enter to(C/K/F): ").lower()
    #Celsius converter
    if from_in == 'c' and to_in == 'k':
      result = 273+temp
      print(f"Your result in kelvin is {result}")
    elif from_in == 'c' and to_in == 'f':
      result = (temp*9/5)+32
      print(f"Your result in Fahrenheit is {result}")
    #kelvin conversions..
    elif from_in == 'k' and to_in == 'c':
      result = temp-273
      print(f"your result in celsius is {result}")
    elif from_in == 'k' and to_in == 'f':
      result = ((temp-273)*9/5)+32
      print(f"Your result in Fahrenheit is {result}")
      # Fahrenheit conversions
    elif from_unit == 'f' and to_unit == 'c':
      result = (temp - 32) * 5/9
      print(f"Your result in Celsius is {result}")
    elif from_unit == 'f' and to_unit == 'k':
      result = ((temp - 32) * 5/9) + 273.15
      print(f"Your result in kelvin is {result}")
    else:
      print("Invalid")
  except ValueError:
    print("Enter valid details.")

      
    
    
    
    
    