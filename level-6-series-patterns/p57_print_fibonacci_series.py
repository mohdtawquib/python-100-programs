# Write a program to display the first n terms of the Fibonacci series.

n = int(input("Enter Nth term : "))

first = 0
second = 1

for i in range(n):
   print(first, end=" ")
   first, second = second, first + second

print()