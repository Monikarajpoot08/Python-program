#  a sentinel value is a special value used to indicate the end of input or to stop a loop. It is not treated as normal data.
#  Common sentinel values are:
#  -1
#  0 (when only positive numbers are expected)
# "exit"
# "quit"
# "done"

sum=0
num=int(input("enter the number(-1 to quit)"))
while num!=-1:   #-1 is a sentinel value used to terminate the loop
    sum=sum+num
    num=int(input("enter the number(-1 to quit)"))
else:
    print("end of the loop")
print(sum)