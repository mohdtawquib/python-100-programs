# Write a program to check whether a number is an automorphic number.

num = int(input("Enter number : "))

square = num ** 2

if str(square).endswith(str(num)):
    print(f"{num} is the automorphic number")
    print(f"Because {num}^2 = {square}")
else:
    print(f"{num} is not automorphic number")