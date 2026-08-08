class Phone:
    followers=0 #class object variable
    mini=9 #class object variable
    def __init__(self,name,address):
        self.name=name
        self.address=address
        #self.followers=0 
    def display(self,sub):
        print(f"hello i am {self.name} and i teach {sub}")

    def update_followers(self,follower_name):
       following_of_this_person=self.followers
       self.followers+=self.followers
       print(f" {follower_name} is now following {self.name}")
       following_of_this_person+=following_of_this_person
       print(f"following of {follower_name} is {following_of_this_person}")
obj1=Phone("ishita","hld")
obj1.display("python")
obj2=Phone("romi","kld")
obj2.display("english")
obj1.update_followers("rishi")
