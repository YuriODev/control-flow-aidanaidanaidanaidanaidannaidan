# Your solution to Exercise 18

if input("do you remember the person's name? ") == 'yes':
  if input('is it an ex? ') == 'yes':
    if input('are you drunk? ') == 'yes':
      if input("do you want to rekindle/give them what for") == 'yes':
        print("Say Hi.")
      elif input("do you want to rekindle/give them what for") == 'no':
        print("Don't Say Hi.")
      else:
        print('????')
    elif input('are you drunk? ') == 'no':
      if input("are you in a convertible with rihanna and/or brad pitt? ") == 'yes':
        print("Say Hi.")
      elif input("are you in a convertible with rihanna and/or brad pitt? ") == 'no':
        print("Don't Say Hi.")
      else:
        print('????')
    else:
      print('????')
  elif input('is it an ex? ') == 'no':
    if input('a friend's ex? ') == 'yes':
      print("Don't Say Hi.")
    elif input('a friend's ex') == 'no':
      if input("an enemy or a frenemy? ") == 'yes':
        if input("are you in a convertible with rihanna and/or brad pitt? ") == 'yes':
          print("Say Hi.")
        elif input("are you in a convertible with rihanna and/or brad pitt? ") == 'no':
          print("Don't Say Hi.")
      elif input("an enemy or a frenemy? ") == 'no':
        if input("are you robbing a bank? ") == 'yes':
          print("Don't Say Hi.")
        elif input("are you robbing a bank? ") == 'no':
          if input("are you in a bathrobe? ") == 'yes':
            print("Don't Say Hi.")
          elif input("are you in a bathrobe? ") == 'no'
            print("Say Hi.")
          else:
            print('????')
        else:
          print('????')
      else:
        print('????')
    else:
      print('????')
  else:
    print('????')
elif input("do you remember the person's name? ") == 'no':
  if input("do you have time to flee? ") == 'yes':
    print("Run For It.")
  elif input("do you have time to flee? ") == 'no':
    if input("could you pretend to get a call? ") == 'yes':
      print("Hello, Doctor, what are my results?")
    elif input("could you pretend to get a call? ") == 'no':
      if input("are you wearing sunglasses? ") == 'yes':
        print("Keep Walking.")
      elif input("are you wearing sunglasses? ") == 'no':
        print('adress the person by calling them a silly name like sarge')
      else:
        print('????')
    else:
      print('????')
  else:
    print('????')
else:
  print('????')
