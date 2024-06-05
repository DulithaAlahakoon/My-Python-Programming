class Vehicle:
  def __init__(self,brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Moving")

class Boat(Vehicle):
  def move(self):
    print("Boat is Sail")

class Car(Vehicle):
  pass

class Plane(Vehicle):
  def move(self):
    print("Plane is Fly")

car1 = Car("Ford", "Mustang")
boat = Boat("Sea Ray", "Sundancer")
plane = Plane("Boeing", "747")

for x in (car1, boat, plane):
  print("Brand: ", x.brand," Model: ", x.model)
  x.move()