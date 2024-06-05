class Person:
  def __init__(self, name, weight, height):
    self.name = name
    self.__bmi = weight/(height**2)

  def walk(self):
    print(self.name, "is walking")

  def getbmi(self):
    return self.__bmi

bob = Person("Bob",60,1.52)
bob.walk()
print(bob.name, "BMI is", bob.getbmi())