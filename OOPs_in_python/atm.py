class ATM:
    def __init__(self):
        self.__pin=''
        self.__balance=0
        #self.menu()
    def menu(self):
        user=int(input("1. Press 1 to create pin\n 2. Print 2 to change pin \n 3. Withdraw \n 4. Deposit - "))
        if user==1:
            self.create_pin()
        elif user == 2:
            print("Changed")
        elif user ==  3:
            self.withdraw()
        elif user ==4:
            self.deposit()
        else:
            print("Thanks")
    def create_pin(self):
        pin=input("Create Pin: ")
        self.__pin=pin
        print("Created")
        self.menu()
    def deposit(self):
        pin=input("Enter pin-")
        if pin==self.__pin:
            amt=int(input("Enter amount-"))
            self.__balance += amt
            print("Deposited")
        else:
            print("invalid")
        self.menu()
    def change_pin(self):
        if self.__pin == '':
            print("Create Pin First")
            self.create_pin()
            self.menu()
    # To change the pin-by another 
    def get__pin(self):
        print(self.__pin)
    def set__pin(self,newpin):
        user=input("Enter pin-")
        self.__pin=user
        print(f"New pin-{self.__pin}")
    def withdraw(self):
        with_amt=int(input("Enter Withdrawl amount"))
        if with_amt<=self.__balance:
            self.__balance -= with_amt
            print("Withdrawl ")
        else:
            print("Error")
        self.menu()
        
std=ATM()

std.get__pin()
std.set__pin(std._ATM__pin)