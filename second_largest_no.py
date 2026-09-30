# Program to find the second largest number
numbers = [10, 45, 23, 89, 67, 89, 34]

# numbers array is converted into set
# set removes the duplicate no.s if present
# then set is converted into list 
unique = list(set(numbers))
unique.sort()
print(unique)

print("Second largest =", unique[-2])