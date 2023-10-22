# function  

# def welcome():
#   print("-"*20)
#   print()
#   print("Welcome to IT industry sir")
#   print()
#   print("*"*20)

## calling in function 
# welcome(kshay)
# welcome()
# welcome()

#printing with user_name (passing the arguments)

# def welcome(user, age=None):
#   print(f"welcome {user}")
#   print(f"age is  {age}")


# welcome("akshay", 27)
# welcome("chiharu")


#Dynmaic Argument Functions 

# def info(name , *hobby): # *var -->> take multiple arguments
#   print(f"name is {name} ")
#   print(f"{name}'s hobbies are ")
#   for i in hobby:
#     print(f"- {i} ")

#   print("*"*25)

# info("akshay", "badminton","cricket")
# info("chiharu" , "badminton" , "training")

 
# return 

def addition(a,b):
  c = a+b
  return c

print(addition(10,20))





  