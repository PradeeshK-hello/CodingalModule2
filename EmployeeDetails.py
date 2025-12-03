class Person(object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
        
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        
        Person.__init__(self,name,idnumber)
        
a = Employee("Pradeesh",90142799,25000,"Computer Science Engineer")
a.display()