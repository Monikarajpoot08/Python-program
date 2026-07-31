#Membership operator is used to check whether a character, substring value,number,or any part is present in a string ,list,tuple,dict or not
#types of this operator (in) and (not in)
str="Monika Rajpoot"
print('i' in str)               #alphabet check
print('ika'  in str)            #substring check
print("Ka"  in str)
print("M" not in str)
print("M" not in "Monika Rajpoot")
#check list
list=[1,2,3,4,5,6]
print(1 in list)
print(2 not in list)