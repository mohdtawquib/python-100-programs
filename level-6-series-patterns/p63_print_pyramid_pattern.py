# Write a program to print a pyramid pattern of stars of height n.

n = int(input("Enter Number : "))

for i in range(1, n+1):
    space = " " * (n-i)
    star = "*" * (2 * i - 1)

    print(space + star)