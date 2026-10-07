# Write a program to read a number and check whether it is positive, negative or zero.

num = int(input("Enter number : "))

if num < 0:
    print(f"{num} is negative")
elif num > 0:
    print(f"{num} is positive")
else:
    print("It's Zero")
