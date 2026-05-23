class Student:
    def __init__(self,name,roll,s1,s2,s3,s4,s5):
        self.name=name
        self.roll=roll
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5
    def sum_of_marks(self):
        c=self.s1+self.s2+self.s3+self.s4+self.s5
        return c
    def average(self,marks):
        aver=marks/5
        print(f"Average of marks={aver}")
    def best_two(self):
        marks=[]
        marks.append(self.s1)
        marks.append(self.s2)
        marks.append(self.s3)
        marks.append(self.s4)
        marks.append(self.s5)
        marks.sort()

        print(marks[-1],marks[-2])



stud=Student("Noor",121,88,76,67,65,45)
av=stud.sum_of_marks()
stud.average(av)
stud.best_two()

 