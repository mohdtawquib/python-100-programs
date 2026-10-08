# Write a program to count the number of factors of a number n.

num = int(input("Enter number : "))
count = 0

print(f"Factorials of the {num} are : ")

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

print(count)