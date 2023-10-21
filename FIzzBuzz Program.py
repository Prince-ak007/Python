#FizzBuzz Program 
"""multiple of 3 ---> Fizz
multiple of 5 ---> Buzz
multiple of 3 and 5 ---> FizzBuzz"""""

#solution 1) without adding into the list
# for i in range(1,25):
#   if i % 3 == 0 and  i % 5 == 0:
#     print("FizzBuzz")
#   elif i % 3 == 0:
#     print("Fizz")
#   elif i % 5 == 0:
#     print("buzz")
#   else:
#     print(i)


#solution 2) adding into the list
my_list = []
for i in range(1,100):
  if i % 3 == 0 and  i % 5 == 0:
    my_list.append("FizzBuzz")
  elif i % 3 == 0:
    my_list.append("Fizz")
  elif i % 5 ==0:
    my_list.append("Buzz")
  else:
    my_list.append(i)
print(my_list)
  







