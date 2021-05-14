from random import randint

class Player:
  def __init__(plantain):
    plantain.dice = []

  def roll(plantain):
    plantain.dice = [] # clears current dice
    for i in range(3):
      plantain.dice.append(randint(1,6))

  def get_dice(plantain):
    return plantain.dice

player1 = Player()
player2 = Player()

player1.roll()
player2.roll()

print("Player 1 rolled" + str(player1.get_dice()))
print("Player 2 rolled" + str(player2.get_dice()))

if sum(player1.get_dice()) == sum(player2.get_dice()):
  print("Draw!")
elif sum(player1.get_dice()) > sum(player2.get_dice()):
  print("Player 1 wins!")
else:
  print("Player 2 wins!")
