#WAP in which: enter a string of 5 names then convert it into a list ,then a random choice among these 5 will be done that who will pay the bill
import random
string=input("enter string")
#split() func coverts the str into list
splitted_str=string.split()
#print(splitted_str)
#splitted_str=string.split("  ")
print(splitted_str)
choice=random.choice(splitted_str)
print(f" {choice} will pay the bill    ")
