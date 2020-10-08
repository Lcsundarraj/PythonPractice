person = 123
price = 100
#'cannot switch from automatic field numbering to manual field specification' error occurs while adding default value in priceS placeholder
Bill = "{1}\'s billing price is {3:.2f} dollars"
print(Bill.format(person,price))




print("``````````````````````````")

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))