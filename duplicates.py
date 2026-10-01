# program to find duplicate elements in a list
numbers = input("Enter numbers separated by space: ").split()

numbers = [int(n) for n in numbers]

duplicates = []

for n in numbers:
    if numbers.count(n) > 1 and n not in duplicates:
        duplicates.append(n)

print("Duplicate elements:", duplicates)