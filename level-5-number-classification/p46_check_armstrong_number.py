# Write a program to check whether a number is an Armstrong number.

def armstrong(n):
    temp = n
    power = len(str(n))
    total_sum = 0

    while temp > 0:
        digit = temp % 10
        total_sum += digit ** power
        temp //= 10

    return n == total_sum


num = int(input("Enter Number to check whether it is Armstrong or not : "))

if armstrong(num):
    print(f"{num} is the Armstrong Number")
else:
    print(f"{num} is not Armstrong Number")

