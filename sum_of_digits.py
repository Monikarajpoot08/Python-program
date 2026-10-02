# Program to calculate the sum of digits of a given number
number = int(input("Enter a number: "))
sum = 0
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10

print("Sum of digits:", sum)