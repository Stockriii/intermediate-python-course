import random

dice_rolls = 2
dice_sum = 0

for i in range(0,dice_rolls):
  roll = random.randint(1,6)
  if roll ==1:
    print(f'You rolled a {roll}! Critical Failure')
  elif roll == 6:
    print(f'You rolled a {roll}! Critical Win')
  else:
    print(f"You rolled a {roll}")
  dice_sum += roll

print(f"This is the sum of both rolls {dice_sum}")