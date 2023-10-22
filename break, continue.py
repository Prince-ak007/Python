# break and continue 

# list = [10, 20, 30, -40, 50, 60, -70, 80, -90, 100]
# for i in list:
#     if i > 0:   #only print +ve values 
#       print(i)
#     else:
#       break


# if msg ==exit -----> quit/ break
while True:
  msg = input("enter the message:   ")
  if msg == "exit":
    break
  else:
    print(msg)