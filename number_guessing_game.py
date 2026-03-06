import random

list1 = []
for i in range(1, 1010):
  list1.append(i)

guess = random.choice(list1)
while True:
  try:
    level = int(input("Level: "))
    break
  except ValueError:
    continue
while True:
  try:
    choice0 = int(input("Guess: "))
    if guess == choice0:
      print("Just right !")
      break
    elif guess < choice0:
      print("Too large !")
      continue
    elif guess > choice0:
      print("Too Small")
      continue
  except ValueError:
    continue
  except KeyboardInterrupt:
    print("fuck you, you can't escape it guess the number first 😎")