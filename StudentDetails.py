class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
    def display(self):
        print(self.fname)
        print(self.lname)

class Student(Person):
    def __init__(self,fname,lname,year,gradyear):
        self.year = year
        self.gradyear = gradyear
        
        super().__init__(fname,lname)
        
    def display2(self):
        print(self.year)
        print(self.gradyear)

Pradeesh = Student("Pradeesh Kumar","Sathish Prabu",8,2030)
Pradeesh.display()
Pradeesh.display2()