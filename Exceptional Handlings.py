# Exceptional Handlings
print(10+2)
try:
  print(10/0) # we know 10/0 ==>> infinity, to solve this error we r doing  this steps..(- _ -)
except ZeroDivisionError:
  print("dont divide using 0")

print(56*2)
print(50-30)


# we will get error if there is no file present to pass or ignore the error we will use "try"...


try:
  with open("user" , "r") as file :
    content = file.rlead()
except FileNotFoundError:
  print("file doesnt exists") 
else:
  for line in content:
    print(f"Welcome {line.estrip()}")

finally:
  print("DB CLOSED")