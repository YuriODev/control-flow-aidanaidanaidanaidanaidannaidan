# Your solution to Exercise 16

d = int(input('enter day: '))
m = int(input('enter month: '))
y = int(input('enter year: '))
if m == 12 or m == 5 or m == 7 or m == 8 or m == 10:
  if d == 1:
    d = 31
    m -= 1
  elif d != 1:
    d -= 1
  else:
    output = 'invalid input'
elif m == 4 or m == 6 or m == 9 or m == 11:
  if d == 1:
    d = 30
    m -= 1
  elif d != 1:
    d -= 1
  else:
    output = 'invalid input'
elif m == 3:
  if d == 1:
    m = 2
    d = 28
  elif d != 1:
    d -= 1
elif m = 1:
  if d == 1:
    m = 12
    d = 31
    y -= 1
  elif d != 1:
    d -= 1
  else:
    output = 'invalid input'
else:
  output = 'invalid input'

if output == '':
  output = f'{d}.{m}.{y}'

print(output)
