import random

# random no. generator between 10 - 30
print (random.randrange(10, 30))




lappy = ["hp", "dell", "lenovo"]
for mine in lappy:
  if mine == "lenovo":
    break
  print(mine) 


a = "Hello, World!"
print(a.lower())

#Tupple Examples
#it gives cherry to kiwi (2-5  excluding 5)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


#change tuple to list (BUT TUPLE IS IMMUTABLE - u can not change values from a tuple)
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#tuple
lappy = ("hp", "dell", "Asus")
print(lappy)
#conert to list
myLappyList = list(lappy)
#modify the value
myLappyList[1] = "Lenovo"
#convert back to tuple
lappy = tuple(myLappyList)

print(lappy)