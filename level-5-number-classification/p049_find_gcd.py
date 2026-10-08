# Write a program to find the GCD (HCF) of two numbers.

import math

num1 = int(input("Enter Number : "))
num2 = int(input("Enter Number : "))

gcd = math.gcd(num1, num2)

print(f"The GCD of {num1} and {num2} are : {gcd}")