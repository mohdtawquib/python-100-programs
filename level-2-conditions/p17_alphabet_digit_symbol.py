# Write a program to read a character and check whether it is an alphabet, digit or special symbol.

input = input("Enter input : ")

# Method 1
# 
# if input.isdigit():
#     print("Input is number")
# elif input.isalpha():
#     print("Input is character")
# else:
#     print("Input is special symbol")

# Method 2

if ('a' <= input <= 'z') or ('A' <= input <= 'Z'):
    print("Input is character")
elif ('0' <= input <= '9'):
    print("Input is number")
else:
    print("Input is special symbol")