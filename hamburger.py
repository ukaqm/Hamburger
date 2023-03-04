#add your name here
#Rai Martin, Thomas Vick, Ezekiel Goodman, Magda Imerlishvili
#Hamburger DoorDash group assignment
#This code takes a list of customers and randomly generates a doordash order then prints their total burgers ordered
import random
#The order class with a method which generates how many burgers the customer ordered
class Order : 

    def __init__ (self) :
        self.burger_count = self.randomBurgers()

    def randomBurgers (self) :
        return random.randrange(1,21)
    
#Person class with a method that randomly selects a customer from the provided list
class Person :

    def __init__ (self) :
        self.customer_name = self.randomName()

    def randomName (self) :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

#Customer class that inherits the person class and initializes an Order object
class Customer(Person) :

    def __init__ (self) :
        super().__init__()
        self.order = Order()

#Creating a dictionary and queue
dictCustomer = {}       
queueCustomers = []

#This loop goes through all 100 customers and adds them to the queue with the oCustomer object
for iCustomers in range(0,100) :
    oCustomer = Customer()
    queueCustomers.append(oCustomer)
    
    #This if statement adds the name to the dictionary as the key, then for that location will increment the customer's burger count
    if oCustomer.customer_name in dictCustomer :
        dictCustomer[oCustomer.customer_name] += oCustomer.order.burger_count 
    else :
        dictCustomer[oCustomer.customer_name] = oCustomer.order.burger_count 

#This creates a new list variable with the customer name and burgers ordered sorted from most ordered to least
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True) 

#This for loop prints each customer with correct alignment from most to least
for customer in listSortedCustomers :
    print(customer[0].ljust(19), customer[1])
