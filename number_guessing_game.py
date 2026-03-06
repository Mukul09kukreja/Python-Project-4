import random

list1 = []
for i in range(1, 101):
  list1.append(i)

guess = random.choice(list1)
while True:
  try:
    level = int(input("Level: "))
    choice = int(input("Guess: "))
    if guess == choice:
      print("Just right")
    if guess != choice:
      print(f"real number is {guess}")
    break
  except ValueError:
    continue