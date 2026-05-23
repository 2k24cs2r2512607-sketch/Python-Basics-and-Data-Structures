# inheritance "is a relationship" -  Bottom to top - "Relationship is must"
class User:#Parent class
# Parent class cannot access methods of child class
    def login(self):
        print("login here")
    def register(self):
        print("register here")
class Student(User):#Child class
    def enroll(self):
        print("course id selected")
    def feedback(self):
        print("review the course")
class Instructor(Student): #Multi-level inheritance
    def create(Self):
        print("create ur course")
    def reply(self):
        print("reply")
# Child class can inherit the instructor,method,attributes(data members) of the parent class except private data members and private method
