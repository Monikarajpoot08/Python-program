#program to find the no of heights in a list and calculate the sum and avg of all heights in the list
list=input("enter  ")
#strings to list conversion
height_list= list.split()
print(height_list)
#find the length of list without len()
count=0
for i in height_list:
    count=count+1
print(count)
for i in range(0,count):
    height_list[i] = int(height_list[i])
print(height_list)
sum=0
for i in height_list:
    sum=sum+i
print("the sum is",  sum)
average=round(sum/count)
print("the average is",average)