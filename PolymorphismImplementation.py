class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
        
    def make_sound(self):
        print("Woof")
    
class Cat:
     def __init__(self,name,age):
        self.name = name
        self.age = age
        
     def info(self):
        print(f"I am a Cat. My name is {self.name}. I am {self.age} years old.")
        
     def make_sound(self):
        print("Meow")
        
ob_dog = Dog("Tessa",3)
ob_cat = Cat("Roxie",5)

for animal in (ob_cat, ob_dog):
    animal.make_sound()
    animal.info()