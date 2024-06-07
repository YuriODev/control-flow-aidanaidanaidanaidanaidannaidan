# Your solution to Exercise 17
num = int(input("Enter a 6 digit number: "))
num1 = num // 100000
num2 = num % 100000 // 10000
num3 = num % 10000 // 1000
num4 = num % 1000 // 100
num5 = num % 100 // 10
num6 = num % 10
if num1 + num2 + num3 == num4 + num5 + num6:
  print("Happy")
else:
  print("Ordinary")
