# python Built-in Module
# 1) random

import random



random_mod = random.random()
print(random_mod)  #Generate random float from 0 to 1  
print(random.randint(1,10)) # int values betn 1 to 10
print(random.uniform(3.5,5.8)) # float values betn 3.5 to 5.8

# Generate a random choice from a list
options = ["apple", "banana","cherry","mango"]
random_choice = random.choice(options)
print(random_choice)

#shuffle
print(options)
random.shuffle(options)
print(options)


#dice game

while True:
  
  print(f"number is {random.randint(1,6)}")
  user = input("do u want to play more y/n :--")
  if user == "n":
    break



