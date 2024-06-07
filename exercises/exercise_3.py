# Your solution to Exercise 3

num = int(input("enter a number 0-36: "))
even = num % 2 == 0
if num == 0:
  print("Green")
elif num >= 1 and num <= 10 and even:
  print("Black")
elif num >= 1 and num <= 10 and not even or num >= 11 and num <= 18 and even:
  print("Red")
elif num >= 11 and num <= 18 and not even or num >= 19 and num <= 28 and even:
  print("Black")
elif num >= 19 and num <= 28 and not even or num >= 29 and num <= 36 and even:
  print("Red")
elif num >= 29 and num <= 36 and not even:
  print("Black")
else:
  print("The bet will not play!")
