# inheritance "is a relationship" -  phone is a product  -  Bottom to top
# Aggregation = "has a relationship" - customer has an address - 
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    def edit_profile(self,new_name,new_gender,new_address):
        self.name=new_name
        self.gender=new_gender
        self.address=new_address
class Address:
    def __init__(self,city,Pin_Code,state):
        self.city=city
        self.pin_code=Pin_Code
        self.state=state
    def change_address(self,new_city,new_Pin_Code,new_state):
        self.city=new_city
        self.pin_code=new_Pin_Code
        self.state=new_state
add=Address("Kanpur",209305,"UP")
add.change_address("Lucknow",202002,"MP")
cust=Customer("Devin","Male",add)                       #Aggregation
cust.edit_profile("Iram","Female",add)
print(cust.address.pin_code)
         
