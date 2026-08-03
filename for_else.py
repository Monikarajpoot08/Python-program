# for-else loop (built-in feature in python only)
# the else block will only execute when the for loop is "successfully" completed
# the below for loop is successfully completed
list=[1,2,3,4,5]
for i in list:
    if i==4:
        continue # the loop will only skip the 3rd index value , overall loop is successfully executed
    print(i)
else:
    print("Successful exit") #this statement will be executed in this case


list=["A","B","C","D","E","F"]
for i in list:
    if i=="D":
        break  # the loop will break from the 4th index hence only A,B,C is printed
               # implies that overall loop is not successfully executed
    print(i)
else:
    print("Successful exit")   #this statement will not execute in this case