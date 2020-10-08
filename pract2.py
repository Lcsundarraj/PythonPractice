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

for x in lappy:
	print(x)



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[2:])

print(len(thislist[2:]))

if "kiwi" in thislist:
  print("Yes, 'kiwi' is in the fruits list")


thislist.insert(5, "papaya")
print(thislist)


print("~~~~~~~~~~~~~~~~~~")

#dictionary example


myCar =  {
  "brand": "Hindustan Motors",
  "model": "Contessa",
  "year": 1984
}
print(myCar)

myCarModel = myCar["model"]
print("model : " + myCarModel )
print("model : " + myCar["model"])
print("model : " + myCar.get("model"))

print("~~~~~~~~~~~~~~~~~~")

myCar["model"] = "Hinustan Contessa"

print("model : " + myCar["model"] )
print(myCar)


for x, y in myCar.items():
  print(x, y)


if "Hinustan Contessa" in myCar.values():
  print("Yes, \'"+ myCar["model"]+"\' model is available")

myCar["color"] = "red"
print(myCar)

for x, y in myCar.items():
  print(x, y)