# Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).

mark = int(input("Enter marks : "))

if mark >= 90:
    print("Grade A")
elif mark >= 70:
    print("Grade B")
elif mark >= 60:
    print("Grade C")
elif mark >= 40:
    print("Grade D")
else:
    print("Fail")
