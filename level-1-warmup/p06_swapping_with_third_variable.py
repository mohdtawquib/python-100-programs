# Write a program to swap two numbers using a third variable

num1 = int(input("Enter Number : "))
num2 = int(input("Enter Number : "))

print("Numbers before swapping : ",num1 ,num2)
temp = num1
num1 = num2
num2 = temp

print("Numbers after swapping : ",num1 ,num2)