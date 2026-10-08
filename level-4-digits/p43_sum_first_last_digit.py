# Write a program to find the sum of the first and last digit of a number n.

n = int(input("Enter n : "))

first = str(n)[0]
last = str(n)[-1]

add = int(first) + int(last)

print(add)