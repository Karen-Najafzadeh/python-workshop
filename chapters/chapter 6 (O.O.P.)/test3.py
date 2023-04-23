class First:
    def __init__(self,name):
        self.name = name

    def show(self):
        print('First')

class Second:

    def Show(self):
        print("Second")


class Third(First, Second):
    def __init__(self,name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def Show(self):
        print(f"{self.name} and {self.last_name} and {self.age}")
    


a = Third('alice','m',12)
a.show()
a.Show()