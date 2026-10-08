# Write a program to print Pascal's triangle for n rows.

n = int(input("Enter Number : "))

for i in range(n):
    print(" " * (n - i), end="")
    coeff = 1
    for j in range(i+1):
        print(coeff, end=" ")
        coeff = coeff * (i - j) // (j + 1)
    print()