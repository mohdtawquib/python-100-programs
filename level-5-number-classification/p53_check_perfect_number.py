# Write a program to check whether a number is a perfect number.

num = int(input("Enter Number : "))

division = 0
for i in range(1, num):
    if num % i == 0:
        division += i

if division == num:
    print(f"{num} is the perfect number") 
else:
    print(f"{num} is not the perfect number")