# Write a program to display all multiples of a number m up to n terms.

n = int(input("Enter the table you want : "))

m = int(input("Enter the terms you want : "))

for i in range(1,m+1):
    print(i*n)