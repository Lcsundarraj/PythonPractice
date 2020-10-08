
file = open("filesample.txt","rt")
print(file.read())

print ("-------------------------")

file = open("filesample.txt","rt")
print(file.read(5))

print ("-------------------------")

file = open("filesample.txt","r")
print(file.readline())

print ("-------------------------")

file = open("filesample.txt","r")
print(file.readline())
print(file.readline())

print ("-------------------------")

file = open("filesample.txt", "r")
for x in file:
  print(x)

print ("-------------------------")


file = open("filesample.txt", "r")
print(file.readline())
file.close()

print ("-------------------------")


file = open("filesample.txt", "a")
file.write("Now the file has more content!")
file.close()

#open and read the file after the appending:
file = open("filesample.txt", "r")
print(file.read())


print("------------------------------")
file = open("newFileSample.txt", "w")
file.write("ooopppsss!! old content deleted")
file.close()

file = open("newFileSample.txt", "r")
print(file.read())

print("------------------------------")
file = open("newFileSample.txt", "w")
file.write("ooopppsss!! sab delete ho gaya")
file.close()

file = open("newFileSample.txt", "r")
print(file.read())



print("-----------------------")
file = open("newFileCreation2", "a")
file.write("Hello Everyone!! Its my new file")
file.write("again i added something")
file.close()

file = open("newFileCreation2","r")
print(file.read())