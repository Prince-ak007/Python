#sets = "{}"===> unordered and unique elements , no duplicate values are allowed ('_')

sets = {"a", "b", "c", "d" , 10 , 50,70, 70,70}
print(type(sets))

# To add
sets.add("e")
print(sets)

# To remove
sets.remove("e")
print(sets)

# TO change list into sets
list = ["a","b" , "c" , "d" , "e" ,"e"]
sets = set(list)
print(sets) # ....... it will give u unique values



