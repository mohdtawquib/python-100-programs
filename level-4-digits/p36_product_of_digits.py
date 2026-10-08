# Write a program to find the product of all digits of a number n.

n = int(input("Enter Number : "))

next = str(abs(n))
multi = 1

for i in next:
    multi *= int(i)
    
print(multi)