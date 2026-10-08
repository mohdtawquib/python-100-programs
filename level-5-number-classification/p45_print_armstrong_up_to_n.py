# Write a program to display all Armstrong numbers from 1 to n.

num = int(input("Enter N term check numbers of Armstrong Numbers between them : "))

for num in range(1, num + 1):
    num_str = str(num)
    power = len(num_str)

    digit_sum = sum(int(digit) ** power for digit in num_str)

    if digit_sum == num:
        print(num)