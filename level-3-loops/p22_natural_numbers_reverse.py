# Write a program to display all natural numbers from 1 to n in reverse order.

n = int(input("Enter n : "))

for i in range(n, 0, -1):
    print(i)
    i += 1
    