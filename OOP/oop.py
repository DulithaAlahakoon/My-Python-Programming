class dog:
  def __init__ (self,name):
    self.name = name

  def bark(self,msg):
    print(self.name + " says " + msg)

dog1 = dog("Tommy")
dog1.bark("Wof Wof")

dog2 = dog("Fido")
dog2.bark("Woof Woof")

