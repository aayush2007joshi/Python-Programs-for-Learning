num = int(input("Enter any positive digit: "))
flag = 0
for i in range(2,num):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print(num, "is not Prime number")
else:
  print(num, "is Prime number")
