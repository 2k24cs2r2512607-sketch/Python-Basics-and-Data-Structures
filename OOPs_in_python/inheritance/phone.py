class Phone:
#private data members and private methods can not be access
    def __init__(self,price,brand,camera):
        print("Inside phone class constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buy a phone")
class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os):
        self.os=os
        super().__init__(price,brand,camera)
        #super() method cannot be access outside the class
    def buy(self):
        print("Buy a smart phone")
        super().buy()
        #Super is a method
        #If this is class has its own constructor then it will call its contructor 
s=SmartPhone(9867,56,34,22)
s.buy()
 

