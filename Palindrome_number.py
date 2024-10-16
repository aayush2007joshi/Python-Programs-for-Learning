num = input("Enter a number: ")
reversed_number = ""
for digit in num:
    reversed_number = digit + reversed_number
if num == reversed_number:
    print(num," is a Palindrome.")
else:
    print(num," is not a Palindrme.")