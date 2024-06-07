# Your solution to Exercise 6
x1 = int(input("enter first value:"))
y1 = int(input("enter second value:"))
x2 = int(input("enter third value:"))
y2 = int(input("enter fourth value:"))
atotal = x1 + y1
btotal = x2 + y2

if x1 == x2 and y1 == y2:
  print("A and B are at the same distance from the origin.")
elif atotal > btotal:
  print("A is further from the origin.")
elif atotal < btotal:
  print("B is further from the origin.")
else:
  pass
