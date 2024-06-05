import random
while True:
  computer = random.randint(0,2)

  player = int(input("Rock, Paper or Scissors? (0 = Rock, 1 = Paper, 2 = Scissors) "))

  if player <0 or player >2:
    print("Wrong Input")
  elif computer == 0 and player == 0:
    print("Computer Choose Rock, You Choose Rock so >>> Tie")
  elif computer == 0 and player == 1:
    print("Computer Choose Rock, You Choose Paper so >>> You Win")
  elif computer == 0 and player == 2:
    print("Computer Choose Rock, You Choose Scissors so >>> You Lose")
  elif computer == 1 and player == 0:
    print("Computer Choose Paper, You Choose Rock so >>> You Lose")
  elif computer == 1 and player == 1:
    print("Computer Choose Paper, You Choose Paper so >>> Tie")
  elif computer == 1 and player == 2:
    print("Computer Choose Paper, You Choose Scissors so >>> You Win")
  elif computer == 2 and player == 0:
    print("Computer Choose Scissors, You Choose Rock so >>> You Win")
  elif computer == 2 and player == 1:
    print("Computer Choose Scissors, You Choose Paper so >>> You Lose")
  elif computer == 2 and player == 2:
    print("Computer Choose Scissors, You Choose Scissors so >>> Tie")
  continue
