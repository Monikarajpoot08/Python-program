# Multiple Inheritance in python
class Human():
    def sleep(self):
        print("i am sleeping")
    '''def eat(self):
        print("i am eating")'''
class Female():
    def dance(self):
        print("i am dancing")
    def eat(self):
        print("eating is fun")
class Child(Human,Female):
        def listen(self):
            print("i am listening")
child=Child()
child.dance()
child.eat()
human=Human()
human.sleep()
