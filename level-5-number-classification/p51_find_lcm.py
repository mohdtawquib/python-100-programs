# Write a program to find the LCM of two numbers.

import math

num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))

lcm = math.lcm(num1, num2)

print(f"The LCM of {num1} and {num2} are : {lcm}")