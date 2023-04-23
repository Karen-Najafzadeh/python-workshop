class Parent:
    species = "homo sapiens"

    def __init__(self,name,age,race):
        self.name = name
        self.age = age
        self.race = race

class Child(Parent):
    
    def __init__(self,name,age,race,job):
        super().__init__(name,age,race)
        self.job = job
        
    def __str__(self):
        return (f"{self.name} ,{self.age}  ,{self.race}  ,{self.job}")

a = Child('ali',12,'german','plummer')
print(a)

