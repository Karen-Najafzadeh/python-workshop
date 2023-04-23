class Applicants:
    entrance_year = 1402
    name_of_organization = "NASA"
    members = []

    def __init__(self, esm, hoghoogh, modat_khedmat):
        self.name = esm
        self.salary = int(hoghoogh)
        self.years = int(modat_khedmat)
    
    # a method to add applicants and save them in tht members list
    @classmethod
    def add(cls,number = int(input("how many you wanna add?\n"))):
        for i in range(number):
            cls.members.append(Applicants(input("what is tour name?\n"),input("how much do you want?\n"),input("which year you were born?\n")))
            print( cls.members[i].name)

    # instance methods does not have access to class attributes but class methods do as shown here        
    # def Hello(self):
    #     print(members)

Applicants.add()

