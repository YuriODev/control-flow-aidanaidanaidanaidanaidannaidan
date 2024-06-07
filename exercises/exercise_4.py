# Your solution to Exercise 4

grade = int(input("enter your grade: "))
if grade > 0 and grade < 4:
  print("initial level")
elif grade > 3 and grade < 7:
  print("average level")
elif grade > 6 and grade < 10:
  print("upper level")
elif grade > 9 and grade < 13:
  print("high level")
else:
  print("level is absent")
