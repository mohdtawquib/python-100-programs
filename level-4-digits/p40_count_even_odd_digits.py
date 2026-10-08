# Write a program to count the number of even digits and odd digits in a number n.

n = int(input("Enter Number : "))

odd = 0
even = 0

for i in str(abs(n)):
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of Odd terms in the number : ", odd)
print("Number of Even terms in the number : ", even)
