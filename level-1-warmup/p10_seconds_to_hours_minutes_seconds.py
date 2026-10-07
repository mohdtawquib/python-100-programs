# Write a program to read seconds and convert them into hours, minutes and seconds.

time = int(input("Enter second : "))

hour = time // 3600
minu = (time % 3600) // 60
sec = time % 60

print(f"{hour} : {minu} : {sec}")