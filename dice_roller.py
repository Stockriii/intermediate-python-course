import random
player_1 = []
player_2 = []
dice_rolls = 2
dice_sum = 0
stop = 0
while stop == 0:
  repeat = 0
  number = int(input("Who is playing 1 or 2"))

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

  if number == 1:
    player_1.append(dice_sum)
  elif number == 0:
    player_2.append(dice_sum)
  else:
    print("Unkown Player; Starting unnoted round; Data won't be stored")
  
  print(f"These are the stats of player 1 {player_1} and player 2 {player_2}")

  while repeat == 0:
    go = str(input("Do you want to go on playing? Yes/No"))

    if go == "Yes":
      stop = 0
      repeat = 1
    elif go == "No":
      stop  = 1
      repeat = 1
    else:
      "Wrong Input"
      repeat = 0