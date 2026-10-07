# Write a program to read three numbers and find the smallest among them.

num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))
num3 = int(input("Enter number : "))

if num1 < num2 and num1 < num3:
    print(f"Number {num1} is the shortest number")
elif num2 < num1 and num2 < num3:
        print(f"Number {num2} is the shortest number")
else:
    print(f"Number {num3} is the shortests number")
