# Write a program to find the product of all natural numbers from 1 to n (factorial of n).

n = int(input("Enter n : "))

multi = 1

for i in range(1, n+1):
    multi *= i

print(multi)