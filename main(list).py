#list
list = ["akshay","bay","cay"]
#adding
list.append("shaa")
print(list)
#removeing
list.remove("shaa")
print(list)
#modify values

list[1] = "kuthe"
print(list)

#insert at particular location 
list.insert(1 , 10)
print(list)

#deleting the value at particular location by using indexing 
del list[1]
print(list)

#length of the list
print(len(list))

#sorting 
list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

#pop  ==>> remove last element as well as give back as a value which we have removed.
list.pop()
list.pop(1)
print(list)


#Numeric List

list_N = [1,3,4,6,7,3,2]

print(min(list_N))
max(list_N)
print(int(sum(list_N)))











                                          