# Write a program to find the value of x raised to the power y without using inbuilt power.

x = float(input("Enter Number : "))
y = int(input("Enter Power : "))

result = 1.0
exp = abs(y)

for i in range(exp):
    result *= x

print(result)