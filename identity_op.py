#identity operators are used to check whether two variables refer to the same object in memory, not just if their values are equal.
#types of identity op :(is) and (is not)
a=3 #a and b will point to the same address hence reusing the memory address
b=3
print(id(a))
print(id(b))
print(a is b)
#memory address reuse the memory for the (same data)
c=5
d=4
print(id(c))
print(id(d))
print(c is d)
print(c is not d)