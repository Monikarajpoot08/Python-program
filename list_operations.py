# LIST METHODS

list=[20,90,89,5,6,9,56]
list.sort() 
print(list)
list.reverse()
print(list)
print(min(list))
print(max(list))
list.append(26) #for inserting value at the end of list (append method takes only one argument)
print(list)
list.extend([78,66]) #to insert more than one value in the list at the end
print(list)
list.insert(2,45) #for inserting value at a particular index
print(list)

#to change only one value in the list
list[0]=34
print(list)

#to change the more than one value in the list in a order 
#list[index from which you want to change: Till length you want to change]
list[1:4]= [2,3,4]
print(list)