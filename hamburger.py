#add your name here
#Rai Martin,
#Hamburger DoorDash group assignment

import random

class Order : 

    def __init__ (self) :
        self.burger_count = self.randomBurgers()

    def randomBurgers (self) :
        return random.randrange(1,21)
    
class Person :

    def __init__ (self) :
        self.customer_name = ""
        self.customer_name = self.randomName()

    def randomName (self) :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

class Customer(Person) :

    def __init__ (self) :
        super().__init__()
        self.order = Order()

dictCustomer = {}       
queueCustomers = []

for iCustomers in range(0,100) :
    oCustomer = Customer()
    queueCustomers.append(oCustomer)
    
    if oCustomer.customer_name in dictCustomer :
        dictCustomer[oCustomer.customer_name] += oCustomer.order.burger_count 
    else :
        dictCustomer[oCustomer.customer_name] = oCustomer.order.burger_count 

listSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True) 

for customer in listSortedCustomers :
    print(customer[0].ljust(19), customer[1])
