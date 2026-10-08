# Write a program to replace all zeros in a number n with the digit 5.

n = int(input("Enter n : "))

print(str(abs(n)).replace('0', '5'))