# Nested list program

list=[1,3,5,[7.6,8,-7],"Monika","harshita"]
print(len(list))
print(list)
#accessing elements of list
print(list[4])
print(list[3])
#accessing the nested list elements
print(list[3][1]) #8 will be printed
#list slicing syntax =  list_name[starting index: upto which length you want to print: steps]
#list_name[i:len:steps]
print(list[0:]) #by default print upto last length
print(list[: 3])# similarly by default starts printing from index 0
print(list[0:4])
print(list[-1])  # -ve index starts from last index
print(list[-2])  #second last
print(list[-3])
print(list[len(list)-1])
#slicing in nested list
print(list[3][0:3])
print(list[3][:])
list_2=[10,34,90,['monika','harshita','ram'],89]
print(list_2)
print(list_2[3][2])