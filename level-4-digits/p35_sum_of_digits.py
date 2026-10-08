# Write a program to find the sum of all digits of a number n.

n = int(input("Enter Number : "))

next = str(abs(n))
sum = 0

for i in next:
    sum += int(i)
    
print(sum)