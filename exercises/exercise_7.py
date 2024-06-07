# Your solution to Exercise 7

num1 = float(input("enter first num: "))
num2 = float(input("enter second num: "))
operation = input("enter operation: ")
if operation == "+":
  print(num1 + num2)
elif operation == "-":
  print(num1 - num2)
elif operation == "*":
  print(num1 * num2)
elif operation == "/":
  if num2 == 0:
    print("Error: division by zero")
  else:
    print(num1 / num2)
elif operation == "mod":
  print(num1 % num2)
elif operation == "pow":
  print(num1 ** num2)
else:
  print("invalid operation")
