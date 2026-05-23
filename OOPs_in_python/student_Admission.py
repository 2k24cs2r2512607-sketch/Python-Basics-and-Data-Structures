#Validate The Data- If marks between 0-100 and age must be greater than 20
#Check Qualified or not - If marks is greater than 65
class Student:
    def __init__(self):
        self.marks=-1
        self.age=-1
        self.validate()
    def validate(self):
        marks=int(input("Enter Your Marks:"))
        age=int(input("Enter Your Age : "))
        if 0<=marks<=100 and age>20:
            self.marks=marks
            self.age=age
            self.qualified()
        else:
            print("Data is invalid")
            return 
    def qualified(self):
        if self.marks>65:
            print("Congratulation!!! You are qualified")
        else:
            print("You are not qualified. Try Luck next time.")
student=Student()
