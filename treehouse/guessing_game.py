import random

random_num = random.randint(1, 10)

for turn in reversed(range(5)):
  try:
    user_num = int(input("Type a number between 1 and 10: "))
  except:
    print("Please enter an whole number!")
    break

  if not user_num > 0 or not user_num < 11:
    print("That number isn't between 1 and 10!\nMy number was %d." % random_num)
    break

  if user_num == random_num:
    print("You guessed right!")
    break
  else:
    if user_num < random_num:
      print("Too low. You have %d chance(s) left!" % turn)
      if user_num < random_num and turn == 0:
        print("Game Over!")
    elif user_num > random_num:
      print("Too high. You have %d chance(s) left!" % turn)
      if user_num > random_num and turn == 0:
        print("Game Over!")
