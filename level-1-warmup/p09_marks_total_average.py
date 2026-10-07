# Write a program to read the marks of 5 subjects and print the total and average.

mark = [] 
sum = 0

for i in range(0,5):
    marks = int(input("Enter you subject marks : "))
    sum = sum + marks
    mark.append(marks)

print("Marks of five subjects : ",mark)
print("Total Marks obtained : ",sum)
print("Average marks per subject : ",sum/5)