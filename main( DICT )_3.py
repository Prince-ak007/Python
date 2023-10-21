#DICTIONARY { key : value }
dict = {
  "akshay" : 10 ,
  "sam" : 20,
  "sativ" : 30,
  "juan" : "90"
}

print(dict)

# calling particular value...
print(dict["sam"])
print("marks of sam " + str(dict["sam"]))
print()
print("marks of juan " + dict["juan"])
print("-------------------------------------")


# .get()
print(".get()")

print(dict.get("akshay"))
print(dict.get("gonzales"))   # if key not present then it will return None

#to add new key and value

dict["sarah"] = 50
print(dict)

#to delete key
del dict["sam"]
print(dict)

print(len(dict))



