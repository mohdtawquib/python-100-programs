# Write a program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2.

n = int(input("Enter Number : "))

sum = 0

for i in range(1, n+1):
    sum += i ** 2

print(f"Sum of the series upto {n}^2 : {sum} ")


