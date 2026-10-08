# Write a program to print a right-angled triangle pattern of stars of height n.

n = int(input("Enter Number : "))

for i in range(1, n+1):
    print("*" * i)