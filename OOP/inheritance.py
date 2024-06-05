class Person:
  def __init__(self, name):
    self.name = name

  def eat(self, food):
    print(self.name + " eats " + food)

  def sleep(self):
    print(self.name + " sleeps")

class Employee(Person):
  def __init__(self, dep):
    self.dep = dep

  def work(self):
    print(self.dep + " works")

  def leave(self):
    print(self.dep + " leaves")


emp1 = Employee("IT")

emp1.name = "Dulitha"
emp1.eat("pizza")
emp1.sleep()
emp1.work()
emp1.leave()
