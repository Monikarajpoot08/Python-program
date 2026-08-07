# __init__() is a special method (also called a constructor) that is automatically called when a new object of a class is created.
#It is mainly used to initialize object attributes.

class A:
    def __init__(self,name,address):
        self.name=name
        self.address=address
a=A("Anjali","karnataka")
print(a.name)
print(a.address)