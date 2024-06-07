# Your solution to Exercise 12

num = input("Enter a number: ")
for i in range(len(num)):
  if num[i] % 2 == 0:
    num[i] = '*'
  else:
    print("Odd")
print(num)
