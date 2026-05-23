import math
class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    def __add__(self,other):
        temp_den=math.lcm(self.den,other.den)
        temp_num=((temp_den//self.den)*self.num)+((temp_den//other.den)*other.num)
        self.num=temp_num
        self.den=temp_den
        if temp_num==0:
            return 0 
        self.simplification()
    def __sub__(self,other):
        temp_den=math.lcm(self.den,other.den)
        temp_num=((temp_den//self.den)*self.num)-((temp_den//other.den)*other.num)
        self.num=temp_num
        self.den=temp_den
        if temp_num==0:
            print(0)
            return 
        self.simplification()
    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        self.num=temp_num
        self.den=temp_den
        self.simplification()
    def __div__(self,other):
        temp_num=self.num*other.den
        temp_den=self.den*other.num
        self.num=temp_num
        self.den=temp_den
        self.simplification()
    def simplification(self):
        temp_num=self.num//math.gcd(self.num,self.den)
        temp_den=self.den//math.gcd(self.num,self.den)
        self.num=temp_num
        self.den=temp_den
        if self.num==self.den:
            print(1)
            return 
        print("{}/{}".format(temp_num,temp_den))  
x=Fraction(2,4)
y=Fraction(2,4)
x*y

# trigonometric 