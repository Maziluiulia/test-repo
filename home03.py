string = input('Enter some text:')
for char in string:
  if char.isdigit() and int(char) % 2 ==0:
    print("It is number and it is even")
  elif  char.isdigit() and int(char) % 2 !=0:
    print("It is number and it is odd")
  elif char.isupper():
    print('capital')
  elif char.islower():
    print('small')
  else:
    print("It is symbol")
