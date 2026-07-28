# Program to find the max value in the list without max method

list=input("enter  ")
#strings to list conversion
max_list= list.split()
print(max_list)
#find the length of list without len()
count=0
for i in max_list:
    count=count+1
print(count)
for i in range(0,count):
    max_list[i] = int(max_list[i])
print(max_list)
maximum=0
for i in max_list:
    if i>maximum:
        maximum=i
print("the maximum no. in the list is ",maximum)