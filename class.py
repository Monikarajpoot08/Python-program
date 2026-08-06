class Instructor:
    def __init__(self):
        print("this is an instructor")

obj1 = Instructor()
obj2 = Instructor()
obj3 = Instructor()
print(type(obj1))  #datatype of object is the class (Instructor)
# As class is the user defined datatype
#all three objects have the Instructor Datatype
print(type(obj2))
print(type(obj3))