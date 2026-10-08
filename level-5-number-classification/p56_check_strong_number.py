# Write a program to check whether a number is a strong number (sum of factorials of its digits).

import math

num = int(input("Enter Number : "))

temp = num
digit_sum = 0

while temp > 0:
    digit = temp % 10
    digit_sum += math.factorial(digit)
    temp //= 10

if num == digit_sum:
    print(f"{num} is the strong number")
else:
    print(f"{num} is the not strong number")
