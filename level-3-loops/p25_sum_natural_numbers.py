# Write a program to find the sum of all natural numbers from 1 to n.

n = int(input("Enter n : "))

sum = 0

for i in range(0,n+1):
    sum += i

print(sum)
