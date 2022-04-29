class Grandparent:
    def __init__(self):
        print("Grandparent")
        super().__init__()

    def do_it(self):
        print("do it: grandparent")

class ParentA(Grandparent):
    def __init__(self):
        print("ParentA")
        super().__init__()

    def do_it(self):
        print("do it: parent a")

class ParentB(Grandparent):
    def __init__(self):
        print("ParentB")
        super().__init__()

    def do_it(self):
        print("do it: parent b")


class Child(ParentA, ParentB):
    def __init__(self):
        print("Child")
        super().__init__()  


child = Child()
child.do_it()

print(Child.__mro__)