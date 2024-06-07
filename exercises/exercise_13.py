# Your solution to Exercise 13

num = int(input("Enter a number: "))
if num <= 9999:
  num1 = num // 1000
  num2 = num % 1000 // 100
  num3 = num % 100 // 10
  num4 = num % 10
  if num1 == num4 or num1 == num3 or num1 == num2:
    print("No")
  elif num2 == num3 or num2 == num4:
    print("No")
  elif num3 == num4:
    print("No")
  else:
    print("Yes")
else:
  pass
