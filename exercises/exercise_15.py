# Your solution to Exercise 15
d = int(input("Enter the day: "))
m = int(input("Enter the month: "))
y = int(input("Enter the year: "))
leapyear = (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0)
if m == 2:
  if leapyear and d == 29:
      day = 1
      month = 3
  elif not leapyear and d == 28:
      day = 1
      month = 3
  elif d < 28 or (leapyear and d < 29):
      d += 1
  else:
      output = "Invalid date"
elif m == 4 or m == 6 or m == 9 or m == 11:
  if d == 30:
    d = 1
    m += 1
  elif d < 30:
    d += 1
  else:
    output = "Invalid date"
elif m == 12:
  if d == 31:
        day = 1
        month = 1
        year += 1
  elif d < 31:
        d += 1
  else:
        output = "Invalid date"
elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10:
  if d == 31:
    d = 1
    m += 1
  elif d < 31:
    d += 1
  else:
    output = "Invalid date"
else:
  output = "Invalid date"
if output == "":
  output = f"{day}.{month}.{year}"
print(output)
