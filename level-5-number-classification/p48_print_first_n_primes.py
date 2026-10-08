# Write a program to display the first n prime numbers.

def prime(n):
    if n <= 0:
        return []

    primes = []
    current_num = 2

    while len(primes) < n:
        is_prime = True

        for i in range(2, int(current_num ** 0.5) + 1):
            if current_num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(current_num)

        current_num += 1

    return primes

num = int(input("Enter n : "))
print(prime(num))




