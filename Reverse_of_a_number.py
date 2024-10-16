num = int(input("Enter any value: "))
temp = num
reverse = 0
while num > 0:
    reminder = num % 10
    reverse = (reverse * 10) + reminder
    num = num // 10
print("Reversed value is: ",reverse)
