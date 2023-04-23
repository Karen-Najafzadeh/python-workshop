class First:
    def __init__(self,name):
        self.name = name

    def show(self):
        print('First')


class Second(First):
    def show(self):
        pass



a = Second('ali')
b = First('mohammad')

a.show()
b.show()