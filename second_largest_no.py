# Program to find the second largest number
numbers = [10, 45, 23, 89, 67, 89, 34]

unique = list(set(numbers))
unique.sort()

print("Second largest =", unique[-2])