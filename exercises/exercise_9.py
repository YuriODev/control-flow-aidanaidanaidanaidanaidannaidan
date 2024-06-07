# Your solution to Exercise 9

num = input("enter a 3 digit number: ")
num2 = int(int(num[0]) + int(num[2]))
num1 = int(num[1])
if num2 == num1:
  print('=')
elif num2 > num1:
  print('>')
else:
  print('<')
