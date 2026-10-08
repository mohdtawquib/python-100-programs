# Write a program to check whether a number n is a palindrome (reads the same reversed).

n = int(input("Enter n : "))

original = str(n)

reverse = str(n)[::-1]

print(original == reverse)

