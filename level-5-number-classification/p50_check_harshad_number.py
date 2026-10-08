# Write a program to check whether a number is a Harshad (Niven) number.

num = int(input("Enter number : "))

if num <= 0:
    print("Please enter positive integer")
else:
    digit_sum = sum(int(digit)for digit in str(num))

if num % digit_sum == 0:
    print(f"{num} is the Harshad (Niven) Number")
    print(f"Because {num} is divisible by {digit_sum}")
else:
    print(f"{num} is not Harshad (Niven) Number")