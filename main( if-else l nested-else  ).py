#if-else
if True: # Or False
  print("it's True")
else:
  print("it's False")


#program 2

if 10 == 8:
  print("true")

else:
  print("False")

#program 3
num = int(input("enter a number to check even or odd :==>>    "))
if num % 2 ==0:
  print("number is even")

else:
  print("number is odd")


#program 4

list = ["akshay","kuthe",10,50]
if "kuthe" in list:
  print("YES, shit is there")


#program 5 to check whether list is empty or not 

list = []

if list:
  print("list is not empty")

else:
  print("list is empty")


# nested if program ==>
voter_id = False
age = 19
if age > 18:
  if voter_id:
    print("you can vote")
  else:
    print("Get the voter id first")
else:
  print("You cant vote")



  