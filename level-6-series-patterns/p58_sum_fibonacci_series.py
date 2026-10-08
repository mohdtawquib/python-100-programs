# Write a program to find the sum of the first n terms of the Fibonacci series.

n = int(input("Enter number : "))

first = 0
second = 1
sum = 0

for i in range(n):
    sum += first
    first, second = second, first + second


print(sum)