#Basic list program
num=[10,0,-4,7] #creating list named num
print(num) 
print(len(num))
print(num[0])
print(num[-1]) #for accessing the last value of the list
print(num[-2]) #for accessing last second value of the list

#List slicing
# num[index : till length] 
print(num[0:4]) 
print(num[:]) #by default it will take i=0 & len=4 (prints the whole list)
print(num[0:])
print(num[:])
print(num[1:3]) 

# similarly if we want to skip any number 
# num[starting index,length,skip part]
print(num[0:4:2])

