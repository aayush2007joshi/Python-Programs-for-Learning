num = int(input("Enter num: "))
fact = 1
if num < 0:
    print("Not Possible")
else:
    for i in range(1, num+1):
        fact = fact * i
print("Factorial of", num, "is", fact)
