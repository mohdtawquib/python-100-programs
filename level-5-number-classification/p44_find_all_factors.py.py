# Write a program to find all factors (divisors) of a number n.

num = int(input("Enter number : "))

print(f"Factorials of the {num} are : ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end = " ")
print()