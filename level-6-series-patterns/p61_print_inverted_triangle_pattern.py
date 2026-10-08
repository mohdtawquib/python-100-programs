# Write a program to print an inverted right-angled triangle pattern of stars of height n.

n = int(input("Enter Number : "))

for i in range(n, 0, -1):
    print("*" * i)