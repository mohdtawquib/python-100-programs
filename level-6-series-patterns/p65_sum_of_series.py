# Write a program to find the sum of the series 1 + 2 + 3 + ... + n.

n = int(input("Enter number : "))
sum = 0

for i in range(1, n+1):
    print(i, end=" ")
    sum += i

print()
print("The sum of the series : ",sum)