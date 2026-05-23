
# Collection of Objects in OOP
# In Object-Oriented Programming (OOP), a collection refers to a group of objects that can be stored and manipulated efficiently. 
class Customer:
    def __init__(self,name):
        self.name=name
    def intro(self):
        print("My name is ",self.name)

c1=Customer("Iram")
c2=Customer("Noor")
c3=Customer("Kevin")
l=[c1,c2,c3]
for i in l:
    i.intro()
 