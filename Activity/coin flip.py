import random

computer = random.randint(0,1)

player = int(input("Heads or Tails?(T = 0 or H = 1) "))

if player <0 or player >1:
  print("Wrong Input")
elif player == computer:
  print("Its",computer,"so You Win")
else:
  print("Its",computer,"so You Lose")