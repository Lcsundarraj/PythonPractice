person = "Raj"
price = 100
#'cannot switch from automatic field numbering to manual field specification' error occurs while adding default value in priceS placeholder
Bill = "{}\'s billing price is {:.2f} dollars"
print(Bill.format(person,price))




print("``````````````````````````")

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))




print("=====================================")
age = 31
name = "Raj"
details = "My name is {1}. I am {0} years old."
print(details.format(age, name))