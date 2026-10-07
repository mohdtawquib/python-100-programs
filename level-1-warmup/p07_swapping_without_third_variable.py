# Write a program to swap two numbers without using a third variable.

num1 = int(input("Enter Number : "))
num2 = int(input("Enter Number : "))

print("Before swapping : ",num1, num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping : ",num1, num2)