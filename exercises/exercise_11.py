# Your solution to Exercise 11

year = int(input("Enter a year: "))
if 1900 ≤ year and year ≤ 3000:
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap")
  else:
    print("Common")
else:
  print("Invalid input")
