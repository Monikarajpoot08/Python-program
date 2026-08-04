#for variable length argument we use positional arbitrary argument
#for example first we pass two arguments(2,3) then three arguments so instead of making different definations of func
#for different functions calls we can use arbitrary arguments

#types of arbitrary arg:

# 1.positional arbitrary arg
# info("monika",18,"playing")
def add(*numbers):
    sum=0
    #the *numbers is a tuple containing the provided arg  every time like (3,4,5)
    print(numbers)
    for i in numbers:
        sum+=i
    print(sum)
add(3,4,5)
add(5,60)
add(0,8,8)

#positional arbitrary arg with keyword arg

def add(*numbers,name): 

    print(numbers)
    print(name)
add(5,60,"monika",name="hlo")





