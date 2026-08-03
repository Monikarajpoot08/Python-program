# .join() Function in python 
tuple=("hi ","My ", "self ", "Monika ")
print(tuple)
s="".join(tuple)  #  .join () concatenates the iterable(list and tuple elements)into a single string
#and you can use commas,space in bw the double quotes to get the desirable values
print(s) #hi My self Monika
s=",".join(tuple) # hi, My, self, Monika
print(s)
