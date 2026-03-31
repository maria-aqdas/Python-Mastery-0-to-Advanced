#Today I learn about "list"
list=["Allah","Almighty", "Prophet", "Muhammad",12, 13.5,True]
print(list)
print(type(list))
#List indexing
print(list[2])   #access 3rd element
print(list[-1])   #access last element
print(list[-2])    #access 2nd lat element

#list slicing
print(list[1:3])   #slincing from index 1 to 2
print(list[::-1])   #reverse list
print(list[0::2])  #stating from and step value is 2
print(list[:3])
print(list[-4:-1])

#Modifying list
list[1]="ALLAH"
print(list)

list.append("My love is 'ALLAH'")
print(list)

list.remove(13.5)
print(list)

#LIST METHODS
#APPEND
fruits=["apple","Banana","charry"]
fruits.append("Mango")
print(fruits)

#EXTAND
fruits=["apple","Banana","charry"]
fruit=["Mango","Orange","Guava"]
fruits.extend(fruit)
print(fruits)

#INSERT
fruits=["apple","Banana","charry"]
fruits.insert(1,"Bulebary")
print(fruits)

#clear
fruits=["apple","Banana","charry"]
fruits.clear()
print(fruits)

#INDEX
fruits=["apple","Banana","charry","Mango"]
index=fruits.index("Mango")
print(index)

#Index with range
fruits=["apple","Banana","Mango","charry","Mango","Bluebary"]
index=fruits.index("Mango",1)
print(index)

#COUNT
fruits=["apple","Banana","Mango","charry","Mango","Bluebary"]
index=fruits.count("Mango")
print(index)

#REVERSE
fruits=["apple","Banana","Mango","charry","Mango","Bluebary"]
fruits.reverse()
print(fruits)

#Sort
a=[3,5,3,2,9,17,846,5,7,90]
a.sort()
print(a)

#in decanding order
a.sort(reverse=True)
print(a)

# # with a key
# a.sort(key=len,reverse=True)
# print(a)

#POP
fruits=["apple","Banana","Mango","charry","Mango","Bluebary"]
poped=fruits.pop(4)
print(poped)
print(fruits)

#POP with no index
fruits=["apple","Banana","Mango","charry","Mango","Bluebary"]
poped=fruits.pop()
print(poped)
print(fruits)

#COPY
#POP
fruits=["apple","Banana","Mango","charry","Mango","Bluebary"]
copyis=fruits.copy()
print(copyis)
print(fruits)

copyis.append("dates")
print(copyis)
print(fruits)