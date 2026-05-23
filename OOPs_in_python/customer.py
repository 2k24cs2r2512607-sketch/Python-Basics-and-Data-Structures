class Customer:
    #class object are mutable datatype
    def __init__(self,name):
        print(id(self))
        self.name=name
def greet(customer):
    # print(id(customer))
    # print(customer.name)#pass by reference
    customer.name="Sote"
cust=Customer("Iram")
l=Customer("Raj")
greet(cust) #pass by reference 
print(id(cust))
print(id(l))
 
 