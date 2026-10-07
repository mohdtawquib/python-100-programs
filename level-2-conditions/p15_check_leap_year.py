# Write a program to read a year and check whether it is a leap year or not.

def is_leap(n):
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    else:
        leap = False
    return leap


year = int(input("Enter year : "))
print(is_leap(year))



