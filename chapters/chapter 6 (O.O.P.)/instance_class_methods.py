class Applicants:
    entrance_year = 1402
    name_of_organization = "NASA"
    members = []

    def __init__(self, esm, hoghoogh, sabeghe):
        self.name = esm
        self.salary = int(hoghoogh)
        self.years = int(sabeghe)

    def __str__(self):
        return(f" this is {self.name} and their salary is {self.salary}")

    # a method to add applicants and save them in tht members list
    @classmethod
    def add(cls,number):
        for i in range(number):
            cls.members.append(Applicants(input("what is tour name?\n"),input("how much do you want?\n"),input("which year you were born?\n")))

    @classmethod
    def All(cls):
        for person in cls.members:
            print(f"{person.name}")
    # a method that shows every saved applicants
    @classmethod
    def Status(cls):
        print("Here is a list of all applicants names")
        for person in cls.members:
            print(person.name)

    # a method that searches all members and see if anybody's salary is under 5M and rises them to 10M
    @classmethod
    def Raise(cls):
        for person in cls.members:
            if person.salary <= 5000000:
                person.salary = 1000000
                print( f"{person.name} had a salary under 5 millions, now it's {person.salary}")

    # a method that checks if the object itself's salary is under 5M and rises them to 10M
    # instance methods does not have access to class attributes but class methods do; as shown here
    def PersonRaise(self):
        if self.salary <= 5000000:
            self.salary = 10000000
            print(f" {self.name}'s salary was under 5M now it's 10 M")
        else:
            print(f"{self.name}'s salary was not higher than 5M so it remains unchanged")



Applicants.add(2)
Applicants.All()
# Applicants.Status()
# Applicants.Raise()
