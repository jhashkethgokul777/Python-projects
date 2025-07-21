class Car:
  def __init__(self, model, manu, year):
    self.model = model
    self.manu = manu
    self.year = year
    self.odometer = 0
  def car_description(self):
    print("This are the details:")
    print(f"The brand is {self.manu}")
    print(f"The model is {self.manu} {self.model}")
    print(f"the year {self.year}")
  def about_odometer(self):
    print(f"The car has {self.odometer} miles on it.")
  def update_odometer(self, miles):
    if miles > self.odometer:
      self.odometer = miles
    else:
      print("You can't roll back..")
  def increment(self, mileage):
    self.odometer += mileage
  def gas_tank(self):
    print("Your gas tank is full")
    
class ElectricCar(Car):
  def __init__(self, model, manu, year):
    super().__init__(model, manu, year)
    self.battery_size = 70
  def about_battery(self):
    print(f"The battery size is {self.battery_size}Kwh.")
  def gas_tank(self):
    print("Your car has no gas tank.")
  
    
    
my_car = Car('i8', 'BMW', '2020')
my_car.car_description()
my_car.gas_tank()
my_tesla = ElectricCar('A5', 'Tesla', '2023')
my_tesla.car_description()
my_tesla.about_battery()
my_tesla.gas_tank()
